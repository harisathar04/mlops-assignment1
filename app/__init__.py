from flask import Flask

app = Flask(__name__)

from app import main  # noqa: F401,E402
