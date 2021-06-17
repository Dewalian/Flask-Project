from mainweb import db
from werkzeug.security import check_password_hash

class Users(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(15), nullable=False, unique=True)
    email = db.Column(db.String(30),nullable=False, unique=True)
    password = db.Column(db.String(60), nullable=False)
    highscore = db.Column(db.Float(), nullable=False)

    def cps(self, passcheck):
        return check_password_hash(self.password, passcheck)
