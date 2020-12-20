from flask import Flask, request, render_template, session, url_for , session , redirect 
from datetime import timedelta 

myapp = Flask(__name__)


myapp.secret_key = "Hello"
myapp.permanent_session_lifetime = timedelta(days=5)




@myapp.route("/" , methods = ["POST" , "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user"))

    else:
        if "user" in session:
            return redirect(url_for("user"))

        return render_template("login.html")




@myapp.route("/user")
def user():
    if  "user" in session :
        # user = session["user"]
        return redirect(url_for("home"))
    else:
        return redirect(url_for("login"))        



@myapp.route('/logout')
def logout():
    session.pop("user")
    return redirect(url_for("login"))
    
    




@myapp.route('/signup')
def signup():
    return render_template('signup.html')




@myapp.route('/home')
def home():
    return render_template('home.html')




@myapp.route('/profile')
def profile():
    if "user" in session:
        return render_template('profile.html')

    else:
        return redirect(url_for("login"))




@myapp.route('/contacts')
def contact_book():
    if "user" in session:
        return render_template('contacts.html')

    else:
        return redirect(url_for("login"))
        



@myapp.route('/about')
def about_us():
    return render_template('about.html')


if __name__ == '__main__':
    myapp.run(debug=True)