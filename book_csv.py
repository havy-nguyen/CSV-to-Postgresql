import os 
import csv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

app = Flask(__name__)

# Set up database
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    author = db.Column(db.String(120), nullable=False)
    year = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Book('{self.id}', '{self.title}', '{self.author}', '{self.year}')"


def writeToDatabase():
  with open('books.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row
    for isbn, title, author, year in reader:
      db.execute



if __name__ == "__main__":
    app.run(debug=True)





