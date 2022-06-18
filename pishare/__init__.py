from flask import Flask, Response, redirect

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile("config.py")

UPLOAD_FOLDER = app.config.get("UPLOAD_FOLDER", "uploads")

if app.config["SECRET_KEY"] == "<YOUR_SECRET_KEY>":
    print("Please change your secret key!")
    print("If you don't know how to generate one, see https://stackoverflow.com/a/54433731.")
    quit(1)

from . import views
app.register_blueprint(views.files)
app.register_blueprint(views.chat)

@app.route("/")
def index() -> Response():
    # TODO: Add home page
    return redirect("/")