from flask import Flask, request, render_template, session, url_for

myapp = Flask(__name__)


@myapp.route('/login')
def login():
    return render_template('login.html')

@myapp.route('/logout')
def logout():
    return '''
    
    '''

@myapp.route('/signup')
def signup():
    return render_template('signup.html')

@myapp.route('/')
def home():
    return render_template('home.html')

@myapp.route('/profile')
def profile():
    return render_template('profile.html')

@myapp.route('/contacts')
def contact_book():
    return render_template('contacts.html')

@myapp.route('/about')
def about_us():
    return render_template('about.html')