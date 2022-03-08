"""The starting point of the app"""
import pathlib
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = pathlib.Path(__file__).parent

app = Flask(__name__)

# database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{basedir}/data-dev.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# pass Exoplanet and User models plus database object to flask shell context
@app.shell_context_processor
def make_shell_context():
    from models import Exoplanet, User
    return dict(
        Exoplanet=Exoplanet,
        db=db,
        User=User,
    )

# import api and models at end to avoid circular import error
import models
import api