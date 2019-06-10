from flask import render_template, redirect, request, session, flash
from config import db, datetime
#from models import User

def index():
    return render_template('index,html')

def nav():
    return render_template('nav.html')

def about():
    return render_template('about.html')

def projects():
    return render_template('projects.html')

def logout():
    session.clear()
    return redirect('/')
