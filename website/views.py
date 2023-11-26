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
    # for hotel in db.session.query(Hotel):   # this will access our db and grab any 'Hotel' object that is stored in there
    #     hotels.append(hotel)
        
    # manually entering in ten different hotels...
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
    
    # if request.method == 'POST':
        
    #     hotel_name = request.form.get('hotel_name')
    #     location = request.form.get('location')
    #     description = request.form.get('description')
        
    #     if len(hotel_name) < 2:
    #         flash('Not a valid hotel name.', category='error')
    #     elif len(location) < 2:
    #         flash('Not a valid location.', category='error')
    #     elif len(description) < 10:
    #         flash('Add more details to description.', category='error')
    #     else:
    #         new_hotel = Hotel(hotel_name=hotel_name, location=location, description=description)
    #         hotels.append(new_hotel)
    #         db.session.add(new_hotel)
    #         db.session.commit()
            
    #         flash('Hotel added successfully!', category='success')
            
    
    return render_template("hotels.html", user=current_user, hotels=hotels)

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
    
    room1 = Room(room_type="Standard", price=400, availability='Yes', hotel_id=1)
    rooms.append(room1)
    room2 = Room(room_type="Deluxe", price=600, availability="Yes", hotel_id=2)
    rooms.append(room2)
    room3 = Room(room_type="Suite", price=800, availability="No", hotel_id=1)
    rooms.append(room3)
    db.session.add(room1)
    db.session.add(room2)
    db.session.add(room3)
    db.session.commit()
    
    return render_template("rooms.html", user=current_user, rooms=rooms)

# delete a room
@views.route('/delete-room', methods=["POST"])
def delete_room():
    pass

# profile page
@views.route('/profile')
@login_required
def profile():
    return render_template("profile.html", user=current_user)



