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



def imageGen(mood):
    # These are all links to the images associated with the mood

    madLink = "https://images.hdqwalls.com/download/mad-joker-4k-0o-1280x1024.jpg"
    sadLink = "This is the sad Link "
    happyLink = "This is the Happy LInk "
    anxiousLink = " This is the anxious Link "
    stressedLink = " This is the Stressed Link "

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
    img = imageGen(mood)
    )
    # return img