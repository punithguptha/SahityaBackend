import os
from flask import Flask
from dotenv import load_dotenv
from pathlib import Path
from .app import app



load_dotenv(Path("local.env"))

user=str(os.getenv('user',"None"))
password=str(os.getenv('password',"None"))
host=str(os.getenv('host',"None"))
database=str(os.getenv('database',"None"))

print(user+" "+password+" "+host+" "+database)

app.config['SQLALCHEMY_DATABASE_URI']=f'postgresql://{user}:{password}@{host}/{database}'

from .models import db
db.init_app(app)

from .import routes
app.register_blueprint(routes.bp)

with app.app_context():
    print("Inside Create All clause")
    db.create_all()