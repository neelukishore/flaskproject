
from flask import Flask, redirect
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy

import os
#from models import Book




project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = 'sqlite:///{}'.format(os.path.join(project_dir, "books.db"))



app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)


# from models import Book
class Book(db.Model):
    title = db.Column(db.String(100), unique=True, nullable=False, primary_key=True)

    

    def __repr__(self):
        return "<Title: {}>".format(self.title)


@app.route("/")
def home():
    books = Book.query.all()
    return render_template("home.html", books=books)

@app.route("/create", methods=["post"])    
def create():
    book = Book(title=request.form.get("title"))  # To add one row
    db.session.add(book)
    db.session.commit()
    return redirect("/")

@app.route("/update", methods=["post"])
def update():
    title = request.form.get("title")
    return render_template("update.html", title=title)    

@app.route("/update_title", methods=["post"])
def update_title():
    old_tile = request.form.get("old_title") 
    new_title = request.form.get("new_title")
    book = Book.query.filter_by(title=old_tile).first()
    book.title = new_title
    db.session.commit()
    return redirect("/")

@app.route("/delete", methods=["post"])
def delete():
    title = request.form.get("title")
    book = Book.query.filter_by(title=title).first()
    db.session.delete(book)    
    db.session.commit()
    return redirect("/")    
    













if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)