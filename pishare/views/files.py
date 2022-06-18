from pathlib import Path

from flask import Blueprint, Response, request, flash, render_template, abort, current_app, redirect
from flask_autoindex import AutoIndexBlueprint, AutoIndex
from werkzeug.utils import secure_filename, safe_join

with current_app.app_context():
    UPLOAD_FOLDER = Path(Path(__file__).parent.parent / current_app.config.get("UPLOAD_FOLDER", "uploads"))

app = Blueprint("files", __name__, url_prefix="/files/")
file_index = AutoIndexBlueprint(app, UPLOAD_FOLDER, add_url_rules=False)

@app.route("/upload/", methods=["POST"])
def upload_file() -> Response:
    if "file" not in request.files:
        print("E")
        return abort(400)
    file = request.files["file"]
    if file.filename == "":
        print("a")
        return abort(400)
    if file:
        filename = secure_filename(file.filename)
        file.save(safe_join(UPLOAD_FOLDER, filename))
    return redirect(f"/files/")


@app.route("/")
@app.route("/<path:path>")
def autoindex(path="."):
    return file_index.render_autoindex(path, template="file_browser.html")