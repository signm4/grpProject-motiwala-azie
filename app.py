'''importing flask server to help deploy'''
import flask
from flask import Flask, flash, redirect, request, url_for, render_template 
# from flask_login import LoginManager, UserMixin, login_user, current_user, login_required
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
                'format' : 'json'}
    )

    json_data = response.json()
    tracks_data = (json_data['tracks'])
    track_data = ((tracks_data['track']))
    return((track_data)["title"])



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