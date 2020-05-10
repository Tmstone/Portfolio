from sqlalchemy.sql import func
from config import *

#database build and methods

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PW_REGEX = re.compile('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$')

class User(bd.Model):
    __tablename__ = "users"
    id = bd.Column(bd.Integer, primary_key = True)
    name = db.Column(db.String(90))
    email = db.Column(db.String(45))
    phone = db.Column(db.String(45))
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    
    def __repr__(self):
        return '<User {}>'.format(self.name)

    @classmethod
    def validate_user(cls, email):
        errors=[]
        existing_users=cls.query.filter(cls.email==email).count()
        if (existing_users)>0:
            errors.append('This email address is already registered!')
        return errors

    @classmethod
    def validate_name(cls, first_name, last_name):
        errors=[]
        if len(name) < 2:
            errors.append('Please enter a valid name (*at least three characters*).')
        return errors
    
    @classmethod
    def validate_email(cls, email):
        errors=[]
        if not EMAIL_REGEX.match(email):
            errors.append('Please enter a valid email.')
        return errors
    
    @classmethod
    def validate_phone(cls, phone):
        errors=[]
        if len(phone) < 7:
            errors.append('Please enter a valid phone number')
        return errors
    
    @classmethod
    def validate_user(cls, attendee_info):
        errors = []
        errors += cls.validate_name(attendee_info['first_name'], attendee_info['last_name'])
        errors += cls.validate_email(attendee_info['email'])
        errors += cls.validate_password(attendee_info['password'], attendee_info['confirm_password'])
        errors += cls.validate_phone(attendee_info['phone'])
        errors += cls.validate_school(attendee_info['school'])
        errors += cls.validate_graduation(attendee_info['graduation'])
        errors += cls.validate_parent(attendee_info['parent_first'], attendee_info['parent_last'] )
        errors += cls.validate_parent_email(attendee_info['parent_email'])
        errors += cls.validate_parent_phone(attendee_info['parent_phone'])
        return errors