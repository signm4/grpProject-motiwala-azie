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
# def imageGen():

'''this function will generate a playlist based on their mood SPOTIFY API '''
# def playlistGen():
