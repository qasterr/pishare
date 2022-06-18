from flask import Blueprint, Response
from flask_socketio import SocketIO

app = Blueprint("chat", __name__)
