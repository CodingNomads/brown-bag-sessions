from app import db
from werkzeug.security import check_password_hash, generate_password_hash


class User(db.Model):
    """The User SQLAlchemy model"""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    confirmed = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<User {self.username}>'

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        """Generate password hash column value when password property set"""
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


class Exoplanet(db.Model):
    """The Exoplanet SQLAlchemy model"""

    __tablename__ = "exoplanets"
    id = db.Column(db.Integer, primary_key=True)
    planet_name = db.Column(db.String(64))
    # planet_link = db.Column(db.String(256))
    host_name = db.Column(db.String(64))
    num_stars = db.Column(db.Integer)
    num_planets = db.Column(db.Integer)
    earth_radius = db.Column(db.Float)
    orbital_period_d = db.Column(db.Float)
    stellar_radius_sr = db.Column(db.Float)
    stellar_distance_pc = db.Column(db.Float)
    year_discovered = db.Column(db.Integer)
    facility = db.Column(db.String(64))
    method = db.Column(db.String(64))
    reference = db.Column(db.String(256))

    @staticmethod
    def insert_exoplanets():
        import util
        df_planets = util.parse_exoplanets("data/PS_2022.03.02_20.05.53.csv")
        util.insert_exoplanets(df_planets, db)

    def to_json(self):
        """Serializes data from the database to a JSON-friendly format"""
        json_exoplanet = {
            'planet_name':              self.planet_name,
            'host_name':                self.host_name,
            'num_stars':                self.num_stars,
            'num_planets':              self.num_planets,
            'earth_radius':             self.earth_radius,
            'orbital_period_d':         self.orbital_period_d,
            'stellar_radius_sr':        self.stellar_radius_sr,
            'stellar_distance_pc':      self.stellar_distance_pc,
            'year_discovered':          self.year_discovered,
            'facility':                 self.facility,
            'method':                   self.method,
            'reference':                self.reference,
        }
        return json_exoplanet
