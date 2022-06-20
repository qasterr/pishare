# PiShare

PiShare is a spiritual successor to the [Piratebox project](https://piratebox.cc/). Its aim is to allow offline sharing of information.

## Features
- File Sharing
- Chat

## Setting up PiShare
### Clone PiShare
```bash
git clone https://github.com/qasterr/pishare.git
cd pishare
```

### Set up a virtual environment
If you don't know how to do this, see [Real Python's introduction to virtual environments](https://realpython.com/python-virtual-environments-a-primer/).

### Install the required dependencies
```bash
pip install -r requirements.txt
```

### Configure PiShare
Create a file named `config.py` in the directory named `instance`.
Copy the configuration from the [Configuration Keys](#configuration-keys) section and change the values you wish to change.

### Starting PiShare
Linux or Mac
```bash
./run.sh
```
Windows
```bash
.\run.bat
```

## Configuration Keys
Example `instances/config.py` file:
```python
SECRET_KEY = "<YOUR_SECRET_KEY>"
UPLOAD_FOLDER = "uploads"
```
### SECRET_KEY
A *secret* key used by Flask. If you do not know how to generate one see [this Stack Overflow answer](https://stackoverflow.com/a/54433731).
### UPLOAD_FOLDER
The name of the folder to use for downloaded files. Will default to `uploads` if not set.

## Open Source Licenses
PiShare is built upon great software by the open source community. These are their licenses.

[Flask](https://flask.palletsprojects.com/) — [BSD-3-Clause License](https://github.com/pallets/flask/blob/main/LICENSE.rst)

[Flask-Autoindex](https://github.com/general03/flask-autoindex) — [MIT License](https://github.com/general03/flask-autoindex/blob/master/LICENSE.md)

[Socket.IO](https://socket.io/) — [MIT License](https://github.com/socketio/socket.io/blob/main/LICENSE)

[Flask-SocketIO](https://github.com/miguelgrinberg/Flask-SocketIO) — [MIT License](https://github.com/miguelgrinberg/Flask-SocketIO/blob/main/LICENSE)

[MarkupSafe](https://github.com/pallets/markupsafe) — [BSD-3-Clause License](https://github.com/pallets/markupsafe/blob/main/LICENSE.rst)

[Flask-SocketIO-Chat](https://github.com/miguelgrinberg/Flask-SocketIO-Chat) — [MIT License](https://github.com/miguelgrinberg/Flask-SocketIO-Chat/blob/master/LICENSE)