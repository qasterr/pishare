from flask import request
from flask_socketio import SocketIO, emit
from markupsafe import escape

# Logic from https://github.com/miguelgrinberg/Flask-SocketIO-Chat

socketio = SocketIO()

def clean_username(username: str) -> str:
    return escape(username[:20])

def clean_message(message: str) -> str:
    return escape(message[:1000])

@socketio.on("joined", namespace="/chat")
def joined(message):
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    emit(
        "status",
        {
            "msg": f"{request.cookies.get('username')} has joined the chat."
        },
        broadcast = True
    )


@socketio.on("text", namespace="/chat")
def text(message):
    """Sent by a client when the user entered a new message.
    The message is sent to all people in the room."""
    if message["msg"] == "":
        return

    emit(
        "message",
        {
            "author": clean_username(request.cookies.get('username')),
            "msg": clean_message(message["msg"])
        },
        broadcast = True
    )