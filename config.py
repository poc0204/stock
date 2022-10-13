from flask import Flask,render_template,redirect,jsonify,url_for,request,session
from flask_socketio import SocketIO, emit
import requests
app=Flask(__name__)