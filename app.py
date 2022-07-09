from crypt import methods
from email import message
from flask import Flask, render_template, request
import sqlite3

import flask

app = Flask(__name__)

@app.route("/")
def my_index_page():
    message = "Login Here"
    return render_template("login.html",message=message)

@app.route("/newuser")
def my_new_userpage():
    return render_template("register.html")

@app.route("/registeruser",methods=['post'])
def my_register_user_page():
    entered_username = request.form.get("username")
    entered_password = request.form.get("password")
    entered_email = request.form.get("email")
    entered_email = entered_email.lower()
    entered_location = request.form.get("location")
    # print(entered_username,entered_password,entered_email,entered_location)
    # return "Hello Riyan"


    con = sqlite3.connect("mydatabase")
    c = con.cursor()
    my_table_query = "create table if not exists userstable(name varchar(50), password varchar(50), email varchar(50), location varchar(50))"
    c.execute(my_table_query)
    c.execute(f"select email from userstable where email='{entered_email}'")
    result = c.fetchone()
    if result!= None:
        message2 = "Email Already Registered! Try to Login"
        return render_template("login.html",message=message2)
    else:
        my_insert_query = f"insert into userstable values('{entered_username}','{entered_password}','{entered_email}','{entered_location}')"    
        c.execute(my_insert_query)
        con.commit()
        return "Successfully Registered"

@app.route("/validateuser",methods=["post"])
def my_validate_page():
    entered_email = flask.request.form.get("email1")
    entered_password = flask.request.form.get("password1")
    entered_email1 = entered_email.lower()
    con = sqlite3.connect("mydatabase")
    c = con.cursor()
    c.execute(f"select * from userstable where email='{entered_email}'and password='{entered_password}' ")
    # return render_template("login.html")
    result = c.fetchone()
    print(result)
    # return "welcome user"
    if result == None:
        message1 = "Invalid Crenditals"
        return render_template("login.html",message=message1)
    else:
        return "welcome user"    







    





if __name__ == "__main__":
    # app.jinja_env.auto_reload = True
    # app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)