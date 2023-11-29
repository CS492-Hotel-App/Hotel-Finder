# file where we'll store most of our views/routes
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Hotel, Room
from . import db 
import json

# we will Blueprints as a way to store our routes
# Blueprint for our views file
views = Blueprint('views', __name__)

# home page
@views.route('/')
def home():
    return render_template("index.html", user=current_user)

# hotels page
@views.route('/hotels', methods=["GET", "POST"])
@login_required
def hotels():
    # create a list of the hotels so that we can pass in this list into our render_template() function so we can access it in hotels.html...
    hotels = []
    
    hotel_images = ['../static/Images/hotel1.jpg',
    '../static/Images/hotel2.jpg',
    '../static/Images/hotel3.jpg',
    '../static/Images/hotel4.jpg',
    '../static/Images/hotel5.jpg',
    '../static/Images/hotel6.jpg',
    '../static/Images/hotel7.jpg',
    '../static/Images/hotel8.jpg',
    '../static/Images/hotel9.jpg',
    '../static/Images/hotel10.jpg']
        
    # to delete the hotels from database.. (for testing purposes...)
    # for hotel in db.session.query(Hotel):
    #     db.session.delete(hotel)
    
    # if the hotel objects are stored in the database, grab them and append them to our hotels list
    for hotel in db.session.query(Hotel):
        hotels.append(hotel)
        
    # if hotels list is empty... that means database has no hotel objects, so create them
    if hotels == []:
        hotel1 = Hotel(hotel_name='Grand Horizon Hotel',location='Chicago, IL',description='Hotel in Chicago, IL',)
        hotels.append(hotel1)
        db.session.add(hotel1)
        
        hotel2 = Hotel(hotel_name='Royal Crest Suites',location='New York, NY',description='Hotel in New York, NY')
        hotels.append(hotel2)
        db.session.add(hotel2)
        
        hotel3 = Hotel(hotel_name='Harmony Haven Hotel',location='Los Angeles, CA',description='Hotel in Los Angeles, CA')
        hotels.append(hotel3)
        db.session.add(hotel3)
        
        hotel4 = Hotel(hotel_name='Metropolitan Grandeur',location='New York, NY',description='Hotel in New York, NY')
        hotels.append(hotel4)
        db.session.add(hotel4)
        
        hotel5 = Hotel(hotel_name='Tranquil Oasis Inn',location='Miami, FL',description='Hotel in Miami, FL')
        hotels.append(hotel5)
        db.session.add(hotel5)
        
        hotel6 = Hotel(hotel_name='Majestic Pines Resort',location='Denver, CO',description='Hotel in Denver, CO')
        hotels.append(hotel6)
        db.session.add(hotel6)
        
        hotel7 = Hotel(hotel_name='Crown Jewel Hotel',location='Chicago, IL',description='Hotel in Chicago, IL')
        hotels.append(hotel7)
        db.session.add(hotel7)
        
        hotel8 = Hotel(hotel_name='Central Park Plaza',location='New York, NY',description='Hotel in New York, NY')
        hotels.append(hotel8)
        db.session.add(hotel8)
        
        hotel9 = Hotel(hotel_name='Golden Gate Grand Hotel',location='San Francisco, CA',description='Hotel in San Francisco, CA')
        hotels.append(hotel9)
        db.session.add(hotel9)
        
        hotel10 = Hotel(hotel_name='Imperial Gardens Hotel',location='Tampa Bay, FL',description='Hotel in Tampa Bay, FL')
        hotels.append(hotel10)
        db.session.add(hotel10)
        
        db.session.commit()

    return render_template("hotels.html", user=current_user, hotels=hotels, hotel_images=hotel_images)

# new route to delete individual hotels
@views.route('/delete-hotel', methods=["POST"])
def delete_hotel():
    hotel = json.loads(request.data)
    hotelId = hotel['hotelId']
    hotel = Hotel.query.get(hotelId)        # look for the hotel with that id..
    
    # if hotel exists.. delete it from db
    if hotel:
        db.session.delete(hotel)
        db.session.commit()
        
    return jsonify({})                      # return nothing

# rooms page
@views.route('/rooms', methods=["GET", "POST"])
@login_required
def rooms():
    rooms = []
    
    # to delete the rooms from database.. (for testing purposes...)
    # for room in db.session.query(Room):
    #     db.session.delete(room)

    # if the room objects are stored in the database, grab them and append them to our hotels list
    for room in db.session.query(Room):
        rooms.append(room)
        
    if rooms == []:
        # Grand Horizon, Chi $$$
        room1 = Room(room_type='Standard', price=150, availability='Yes', hotel_id=1)
        rooms.append(room1)
        room2 = Room(room_type='Deluxe', price=400, availability='Yes', hotel_id=1)
        rooms.append(room2)
        room3 = Room(room_type='Suite', price=800, availability='No', hotel_id=1)
        rooms.append(room3)
        
        # Royal Crest, NY $$
        room4 = Room(room_type='Standard', price=100, availability='Yes', hotel_id=2)
        rooms.append(room4)
        room5 = Room(room_type='Deluxe', price=200, availability='Yes', hotel_id=2)
        rooms.append(room5)
    
        # Harmony, LA $$$
        room6 = Room(room_type='Standard', price=200, availability='Yes', hotel_id=3)
        rooms.append(room6)
        room7 = Room(room_type='Deluxe', price=350, availability='Yes', hotel_id=3)
        rooms.append(room7)
        room8 = Room(room_type='Suite', price=800, availability='Yes', hotel_id=3)
        rooms.append(room8)
        
        # Metro, NY $$$
        room9 = Room(room_type='Standard', price=200, availability='Yes', hotel_id=4)
        rooms.append(room9)
        room10 = Room(room_type='Deluxe', price=400, availability='Yes', hotel_id=4)
        rooms.append(room10)
        room11 = Room(room_type='Suite', price=800, availability='No', hotel_id=4)
        rooms.append(room11)
        
        # Tranquil, Miami $$$
        room12 = Room(room_type='Standard', price=200, availability='Yes', hotel_id=5)
        rooms.append(room12)
        room13 = Room(room_type='Deluxe', price=400, availability='Yes', hotel_id=5)
        rooms.append(room13)
        room14 = Room(room_type='Suite', price=800, availability='No', hotel_id=5)
        rooms.append(room14)
        
        # Majestic, CO $$
        room15 = Room(room_type='Standard', price=100, availability='Yes', hotel_id=6)
        rooms.append(room15)
        room16 = Room(room_type='Deluxe', price=150, availability='Yes', hotel_id=6)
        rooms.append(room16)
        
        # Crown, Chi $$
        room17 = Room(room_type='Standard', price=100, availability='Yes', hotel_id=7)
        rooms.append(room17)
        room18 = Room(room_type='Deluxe', price=150, availability='Yes', hotel_id=7)
        rooms.append(room18)
        
        # Central, NY $$
        room19 = Room(room_type='Standard', price=100, availability='Yes', hotel_id=8)
        rooms.append(room19)
        room20 = Room(room_type='Deluxe', price=150, availability='Yes', hotel_id=8)
        rooms.append(room20)
        
        # Golden, SF $$
        room21 = Room(room_type='Standard', price=100, availability='Yes', hotel_id=9)
        rooms.append(room21)
        room22 = Room(room_type='Deluxe', price=150, availability='Yes', hotel_id=9)
        rooms.append(room22)
        
        # Imperial, Tampa $
        room23 = Room(room_type='Standard', price=50, availability='Yes', hotel_id=10)
        rooms.append(room23)
        
    for room in rooms:
        db.session.add(room)
        # db.session.commit()
        
    hotel_names = []
    for room in rooms:
        hotel_name = get_hotel_name(room.hotel_id)
        hotel_names.append(hotel_name)

    db.session.commit()
    
    return render_template("rooms.html", user=current_user, rooms=rooms, hotel_names=hotel_names)

# function to get the hotel name of each room
def get_hotel_name(hotel_id):
    hotel_name = Hotel.query.filter_by(id=hotel_id).first().hotel_name
    return hotel_name

# delete a room
@views.route('/delete-room', methods=["POST"])
def delete_room():
    pass

# booking form page
@views.route('/booking', methods=["GET", "POST"])
def booking():
    
    return render_template("booking.html", user=current_user)

# profile page
@views.route('/profile')
@login_required
def profile():
    return render_template("profile.html", user=current_user)



