from sqlalchemy.sql import func
from config import *

#database build and methods

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PW_REGEX = re.compile('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$')

class Contact(bd.Model):
    __tablename__ = "contact"
    id = bd.Column(bd.Integer, primary_key = True)
    name = db.Column(db.String(90))
    email = db.Column(db.String(45))
    phone = db.Column(db.String(45))
    message = db.Column(db.String(225))
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    
    def __repr__(self):
        return '<Contact {}>'.format(self.name)

    @classmethod
    def validate_contact(cls, email):
        errors=[]
        existing_contact=cls.query.filter(cls.email==email).count()
        if (existing_contact)>0:
            errors.append('This email address is already registered!')
        return errors

    @classmethod
    def validate_name(cls, name):
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
    def validate_contact(cls, contact_info):
        errors = []
        errors += cls.validate_name(contact_info['name'])
        errors += cls.validate_email(contact_info['email'])
        errors += cls.validate_phone(contact_info['phone'])
        return errors
    
    @classmethod
    def add_contact(cls, contact_info):    
        new_contact = cls (
            first_name=contact_info['name'], 
            email=contact_info['email'], 
            phone=contact_info['phone'],
            message=contact_info['message']
            )
        db.session.add(new_attendee)
        db.session.commit()
        return new_contact