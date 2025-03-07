from flask import Flask

app = Flask(__name__)

import app.main  # noqa: F401,E402
