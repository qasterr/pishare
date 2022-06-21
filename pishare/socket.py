from flask import request
from flask_socketio import SocketIO, emit
from markupsafe import escape

# Logic from https://github.com/miguelgrinberg/Flask-SocketIO-Chat

socketio = SocketIO()

def trim_and_escape(message: str, trim_length: int) -> str:
    """Trim a message to `trim_length` characters and escape
    it if HTML tags are included."""
    return escape(message[:trim_length])


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
            "author": trim_and_escape(request.cookies.get('username'), 20),
            "msg": trim_and_escape(message["msg"], 2000)
        },
        broadcast = True
    )