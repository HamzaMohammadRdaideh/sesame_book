from flask import Flask, request, render_template, session, url_for, session, redirect, flash 
from datetime import timedelta 

myapp = Flask(__name__)

myapp.secret_key = ".13456356sdfHello"
# myapp.permanent_session_lifetime = timedelta(days=5)

@myapp.route('/')
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


@myapp.route("/login", methods = ["POST" , "GET"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        # session.permanent = True
        user = request.form["username"]
        session["user"] = user
        flash("You were successfully logged in.", "info")
        return redirect(url_for("profile"))


@myapp.route('/logout')
def logout():
    session.pop("user", None)
    flash("You were successfully logged out.", "info")
    return redirect(url_for("login"))


if __name__ == '__main__':
    myapp.run(debug=True)