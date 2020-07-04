import os 
import csv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

engine = create_engine(os.getenv("DATABASE_URL"))
database = scoped_session(sessionmaker(bind=engine))

app = Flask(__name__)

# Set up database
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(30), nullable=False)
    title = db.Column(db.String(150), nullable=False)
    author = db.Column(db.String(120), nullable=False)
    year = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Book('{self.id}', '{self.isbn}', '{self.title}', '{self.author}', '{self.year}')"


def writeToDatabase():
    with open('books.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader) # Skip the header row
        for isbn, title, author, year in reader:
            database.execute("INSERT INTO book (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)",
                        {"isbn": isbn, "title": title, "author": author, "year": year}) 
            print(year)
    database.commit()
    

writeToDatabase()
print("done")







