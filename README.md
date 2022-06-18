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
```bash
py run.py
```

## Configuration Keys
Example `instances/config.py` file:
```python
SECRET_KEY = "<YOUR_SECRET_KEY>"
UPLOAD_FOLDER = "/uploads"
```
### SECRET_KEY
A *secret* key used by Flask. If you do not know how to generate one see [this Stack Overflow answer](https://stackoverflow.com/a/54433731).
### UPLOAD_FOLDER
The name of the folder to use for downloaded files. Will default to `/uploads` if not set.