from flask_socketio import SocketIO, emit
from markupsafe import escape

# Logic from https://github.com/miguelgrinberg/Flask-SocketIO-Chat

PLACEHOLDER_NAME = "John Doe"

socketio = SocketIO()

@socketio.on("joined", namespace="/chat")
def joined(message):
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    emit(
        "status",
        {
            "msg": f"{PLACEHOLDER_NAME} has joined the chat."
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
            "author": PLACEHOLDER_NAME,
            "msg": escape(message["msg"])
        },
        broadcast = True
    )