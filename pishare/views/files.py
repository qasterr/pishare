"""The file sharing module for PiShare."""

from pathlib import Path
from flask import Blueprint, Response, request, flash, render_template, abort, current_app, redirect
from flask_autoindex import AutoIndexBlueprint, AutoIndex
from werkzeug.utils import secure_filename, safe_join

import pishare

UPLOAD_FOLDER = Path(Path(__file__).parent.parent / pishare.UPLOAD_FOLDER)

files = Blueprint("files", __name__, url_prefix="/files/")
file_index = AutoIndexBlueprint(files, UPLOAD_FOLDER, add_url_rules=False)

@files.route("/upload/", methods=["POST"])
def upload_file() -> Response:
    """Upload the file in a POST request to the upload folder."""
    if "file" not in request.files:
        print("E")
        return abort(400)
    file = request.files["file"]
    if file.filename == "":
        return abort(400)
    if file:
        filename = secure_filename(file.filename)
        file.save(safe_join(UPLOAD_FOLDER, filename))
    return redirect(f"/files/")


@files.route("/")
@files.route("/<path:path>")
def autoindex(path: str = ".") -> Response:
    """Render a file browser for the files in the upload directory."""
    return file_index.render_autoindex(path, template="file_browser.html")