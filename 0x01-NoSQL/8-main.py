#!/usr/bin/env python3
""" 8-main """
from dotenv import load_dotenv, find_dotenv
import os
import pprint
from pymongo import MongoClient
load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")

connection_str = f"mongodb+srv://njoro:{password}@cluster0.aiekeau.mongodb.net/"

list_all = __import__('8-all').list_all

if __name__ == "__main__":
    client = MongoClient(connection_str)
    school_collection = client.my_db.school
    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {}".format(school.get('_id'), school.get('name')))