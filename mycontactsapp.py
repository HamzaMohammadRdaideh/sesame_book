from flask import Flask, request, render_template, session, url_for, session, redirect, flash 
from datetime import timedelta 
import datetime

myapp = Flask(__name__)
user = None
email= None
today = datetime.date.today()
myapp.secret_key = ".13456356sdfHello"
myapp.permanent_session_lifetime = timedelta(days=1)

contacts_dictionary={
    "contact":[ {"name" : "Elmo","phone_number":"0785121254"},
                {"name" : "CookieMonster","phone_number":"0775292323"},
                {"name" : "Bert","phone_number":"0779632147"},
                {"name" : "Ernie","phone_number":"079512789"},
                {"name" : "kermit the Frog","phone_number":"0775893214"}
			]}




@myapp.route('/')
def home():
    return render_template('home.html')


@myapp.route('/view/<int:index>')
def view(index):
    global time
    view_contact = contacts_dictionary['contact'][index -1]
    return render_template('view.html', contact = view_contact,  today = today )

    



@myapp.route('/edit', methods=["POST","GET"])
def edit():
    if request.method == 'GET':
        return render_template("edit.html", dictionary=contacts_dictionary)
    else:

        contactname = request.form['contactname']
        contactnumber = int(request.form['contactnumber'])
        index = int(request.form['index'])

        contacts_dictionary['contact'][index -1].update({'name':contactname,'phone_number':contactnumber})
        return redirect(url_for("contact_book"))




@myapp.route('/add', methods=["POST","GET"])
def add():
    if request.method == "GET":
        return render_template('add.html')
    else:
        contactname = request.form['contactname']
        contactnumber = request.form['contactnumber']
        contacts_dictionary['contact'].append({'name':contactname,'phone_number':contactnumber})
        return redirect(url_for('contact_book'))



@myapp.route('/delete', methods=["GET", "POST"])
def delete():
    if request.method == 'GET':
        return render_template("delete.html", dictionary=contacts_dictionary)
    else:
        contactnumber = int(request.form['contactnumber'])
        contacts_dictionary['contact'].pop(contactnumber - 1)

        return redirect(url_for("contact_book"))



@myapp.route('/profile')
def profile():
    if "user" in session:            
        return render_template('profile.html',user = user,email = email)

    else:
        return redirect(url_for("login"))




@myapp.route('/contacts')
def contact_book():
    if "user" in session:
        return render_template('contacts.html',user=user, dictionary=contacts_dictionary)

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
        session.permanent = True
        global user
        global email
        user = request.form["username"]
        email = request.form["email"]
        session["user"] = user
        session["email"] = email
        flash("You were successfully logged in.", "info")
        return redirect(url_for("profile"))



@myapp.route('/logout')
def logout():
    session.pop("user", None)
    flash("You were successfully logged out.", "info")
    return redirect(url_for("login"))



if __name__ == '__main__':
    myapp.run(debug=True)