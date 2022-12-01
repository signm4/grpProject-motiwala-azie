'''importing flask server to help deploy'''
import flask
from flask import Flask, flash, redirect, request, url_for, render_template 

from flask_login import LoginManager, UserMixin, login_user, current_user, login_required

'''importing os to get env key from other file'''
import os

'''importing requests to use for API'''
import requests
# pip install requests

'''import flask sql'''
# from flask_sqlalchemy import SQLAlchemy, session

import random
from dotenv import load_dotenv
# pip install python-dotenv



app = Flask(__name__)

# login_manager = LoginManager()
# login_manager.login_view = 'auth.login'
# login_manager.init_app(app)

# class Person(UserMixin, db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique = True, nullable = False)

#     def __repr__(self):
#         return '<Review %r>' % self.username

#     def __repr__(self) -> str:
#         return f"Person with username: {self.username}"


# @login_manager.user_loader
# def load_user(id):
#     # since the user_id is just the primary key of our user table, use it in the query for the user
#     return Person.query.get(int(id))

@app.route('/')
def index():
    return render_template('index.html')

'''this function will generate an image based on the following mood that they choose'''
# need this to generate a link and then somehow get it posted in the css file
#if not css then to the html
# @app.route('/handle_mood_pic', methods = ['POST'])
# def moodHandler():
#     form_data = request.form
#     mood = form_data['mood']
#     imageGen(mood)
#     return flask.render_template('index.html')

def playlistGen(mood):
    if (mood == "happy"):
        trackVal = 900000
        trackArs = 100000

    elif (mood == "mad"):
        trackVal = 0
        trackArs =0

    elif (mood == "sad"):
        trackVal = 0
        trackArs =0

    elif (mood == "anxious"):
        trackVal = 500000
        trackArs = 500000

    elif (mood == "stressed"):
        trackVal = 200000
        trackArs = 500000

    MUSICOVERY_API_REQUEST = 'http://musicovery.com/api/V6/playlist.php?'
    response = requests.get(
        f"{MUSICOVERY_API_REQUEST}",
        params={'fct':'getfrommood',
                'resultsnumber' : 5,
                'trackvalence' : trackVal,
                'trackarousal' : trackArs,
                'format' : 'json'},
                verify=False
    )
    td_array = []
    json_data = response.json()
    tracks_data = (json_data['tracks'])
    track_data = ((tracks_data['track']))
    for i in track_data:
        title_data = (i['title'])
        # td_array.append((track_data['title']))
        # print((title_data)['title'])
        return(title_data)




def imageGen(mood):
    # These are all links to the images associated with the mood

    madLink = "https://images.hdqwalls.com/download/mad-joker-4k-0o-1280x1024.jpg"
    sadLink = "https://wallpaperset.com/w/full/5/0/f/205832.jpg"
    happyLink = "https://i.pinimg.com/736x/c5/c5/32/c5c5328c711e890dac56b5fd63160623.jpg"
    anxiousLink = "https://i0.wp.com/post.medicalnewstoday.com/wp-content/uploads/sites/3/2021/06/debilitating_anxiety_GettyImages1141651689_Header-1024x575.jpg?w=1155&h=1528"
    stressedLink = "https://wallpapercave.com/wp/wp5538491.jpg"

    if( mood == "mad"):
        return madLink
        
    elif ( mood == "sad"):
        return sadLink 
        
    elif (mood == "happy"):
        return happyLink

    elif (mood == "anxious"):
        return anxiousLink

    elif (mood == "stressed"):
        return stressedLink

'''this function will generate a playlist based on their mood SPOTIFY API '''
# def playlistGen():

@app.route('/index.html', methods = ["POST"])
def main():
    mood = request.form.get('mood')
    # mood = moodHandler()
    return flask.render_template(
        'index.html',
    # mood = "mad",
    img = imageGen(mood),
    playlistLink = playlistGen(mood)
    )
    # return img


# @app.route('/handle_login', methods = ['POST'])
# def handle_login():
#     username = request.form.get('username')
#     if username == " ":
#         flash("Invalid, Please try again")
#         return redirect(url_for('login'))
#     person = Person.query.filter_by(username = username).first()
#     global curr_user
#     curr_user = username
#     # Person.query.filter_by(username)
#     if person:
#         login_user(person)
#         print("User Accepted")
#         return redirect(url_for('main'))
#     else:
#         flash("Failed Identity, Try again")
#         print("User Declined")
#         return(redirect(url_for('login')))
        
#     # return flask.redirect(url_for('welcome'))



# @app.route('/handle_signup', methods = ['POST'])
# def handle_signup():

#     # 
#     if request.method == "POST":
#         # getting input with name = fname in HTML form
#         username = request.form.get("username")
#         auth_user = Person(username = username)
#         db.session.add(auth_user)
#         db.session.commit()
#         # flash( "Your name is "+ username )
#         return redirect(url_for('login'))
#         # return render_template("index.html")
#     # return flask.redirect(url_for('welcome'))