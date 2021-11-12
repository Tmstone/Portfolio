from flask import render_template, redirect, request, session, flash
from config import db, datetime
from models import Contact

def index():
    return render_template('index.html')

def nav():
    return render_template('nav.html')

def footer():
    return render_template('footer.html')

def about():
    return render_template('about.html')

def projects():
    return render_template('projects.html')

def contact():
    return render_template('contact.html')

def new_contact():
    #submit data to db
    #use ajax for confirmation
    errors = Contact.validate_contact(request.form)
    if errors:
        for error in errors:
            flash(error)
        return redirect('/contact')
    contact = Contact.add_contact(request.form)
    session['contact_id'] = contact.id
    return redirect('/')
    
def login():
    return render_template('login.html')

def logout():
    session.clear()
    return redirect('/')
