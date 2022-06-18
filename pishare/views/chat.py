from datetime import datetime
from flask import Blueprint, Response, render_template, current_app
from flask_socketio import emit

chat = Blueprint("chat", __name__)

@chat.route("/chat/")
def chat_template():
    return render_template("chat.html")
