from flask import Flask

from routes import to_do_bp
from models import db
import os
from api import api_bp


app=Flask(__name__)

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "your_secret_key")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///to_do.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app) 

with app.app_context():
    db.create_all()

app.register_blueprint(to_do_bp)
app.register_blueprint(api_bp,url_prefix='/api')

if __name__=='__main__':
    app.run(debug=True)