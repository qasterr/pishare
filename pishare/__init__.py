from flask import Flask, Response, render_template
from .socket import socketio

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile("config.py")

if app.config["SECRET_KEY"] == "<YOUR_SECRET_KEY>":
    print("Please change your secret key!")
    print("If you don't know how to generate one, see https://stackoverflow.com/a/54433731.")
    quit(1)

UPLOAD_FOLDER = app.config.get("UPLOAD_FOLDER", "uploads")

@app.route("/")
def index():
    return render_template("index.html")

from . import views
app.register_blueprint(views.files)
app.register_blueprint(views.chat)

socketio.init_app(app)