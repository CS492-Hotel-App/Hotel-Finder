# file to store our database models
from . import db 
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(1000), unique=True)
    name = db.Column(db.String(1000))
    password = db.Column(db.String(1000))
    bookings = db.relationship('Booking')
    
class Hotel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hotel_name = db.Column(db.String(1000))
    location = db.Column(db.String(1000))
    description = db.Column(db.String(1000))
    rooms = db.relationship('Room')             # hotel has a one to many relationship with rooms
    
class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room_type = db.Column(db.String(1000))
    price = db.Column(db.Integer)
    availability = db.Column(db.String(1000))
    hotel_id = db.Column(db.Integer, db.ForeignKey('hotel.id'))     # foreign key for Room class
    
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    check_in_date = db.Column(db.Date())
    check_out_date = db.Column(db.Date())
    hotel_name = db.Column(db.String(1000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    