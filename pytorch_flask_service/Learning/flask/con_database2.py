from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config
from datetime import datetime

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)

class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    publishing_office = db.Column(db.String(50), nullable=False)
    isbn = db.Column(db.String(50), nullable=False)
    storage_time = db.Column(db.DateTime, default=datetime.now())
db.create_all()


if __name__ == '__main__':
    app.run()