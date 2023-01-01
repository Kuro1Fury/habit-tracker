import os
from flask import Flask
from routes import pages
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()


def create_app():
    app = Flask(__name__)

    client = MongoClient(os.environ.get("MONGODB_URI"))
    # client = MongoClient(
    #     "mongodb+srv://Kuro1_Fury:skycoder135790@habittracker.pkjfjjn.mongodb.net/test")
    app.db = client.Habits

    app.register_blueprint(pages)

    return app
