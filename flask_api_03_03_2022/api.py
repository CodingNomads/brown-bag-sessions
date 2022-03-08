"""The API"""
from sqlalchemy import false
from models import Exoplanet, User
from app import app
from flask import jsonify
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

# defines a GET endpoint at /exoplanets
@app.route('/exoplanets/', methods=["GET"])
# requires user of API to pass in email and password
@auth.login_required
def get_exoplanets():
    """return all exoplanets' info as JSON"""
    exoplanets = Exoplanet.query.all()
    return jsonify({'exoplanets': [exoplanet.to_json() for exoplanet in exoplanets]})

# this is what gets called when user passes email and password (basic auth)
# when making API request
@auth.verify_password
def verify_password(email, password):
    if email == '':
        return False
    if password == '':
        return False
    user = User.query.filter_by(email=email).first()
    if user is None:
        return False
    return user.verify_password(password)
