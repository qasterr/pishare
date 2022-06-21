"""The chat module for PiShare."""

from datetime import datetime
from flask import Blueprint, Response, render_template, current_app, request, redirect, make_response, abort
from flask_socketio import emit

chat = Blueprint("chat", __name__, url_prefix="/chat/")

@chat.route("/")
def chat_template() -> Response:
    """Render the chat application."""
    if request.cookies.get("username") is None:
        return redirect("/chat/login/")
    return render_template("chat.html")


@chat.route("/login/", methods=["GET", "POST"])
def chat_login() -> Response:
    """Set a cookie with the username if a valid POST request is made
    or render a page for choosing a username."""
    if request.method == "POST":
        form = request.form
        username = form.get("username")

        if username is not None:
            if username != "":
                if len(username) > 20:
                    return render_template("chat_login.html", error="Username too long")
                else:
                    resp = make_response(redirect("/chat/"))
                    resp.set_cookie("username", value=username)
                    return resp
            else:
                return render_template("chat_login.html", error="Username cannot be empty")
        return abort(400)
    elif request.cookies.get("username") is not None:
        return redirect("/chat/")
    else:
        return render_template("chat_login.html")