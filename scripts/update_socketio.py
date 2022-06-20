from pathlib import Path
import requests

SCRIPT_PATH = Path(Path(__file__).parent.parent / "pishare" / "static" / "socket.io.min.js")

if __name__ == "__main__":
    req = requests.get("https://cdn.socket.io/4.5.0/socket.io.min.js")
    if not SCRIPT_PATH.exists():
        SCRIPT_PATH.touch()

    with open(SCRIPT_PATH, "wb") as f:
        f.truncate()
        f.write(req.content)