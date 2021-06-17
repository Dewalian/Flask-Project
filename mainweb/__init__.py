from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///memory.db"
app.config["SECRET_KEY"] = "6b5545a44ccff9a6fa29357e8b6608eb78bb8244ca487667"
db = SQLAlchemy(app)

from mainweb import routes