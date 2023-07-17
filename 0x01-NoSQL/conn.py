#!/usr/bin/env python3
from dotenv import load_dotenv, find_dotenv
import os
import pprint
from pymongo import MongoClient
load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")

connection_str = f"mongodb+srv://njoro:{password}@cluster0.aiekeau.mongodb.net/"
client = MongoClient(connection_str)

#all the databses
databases = client.list_database_names()
print(databases)
#access the database
test_db = client.test
#list all the collections in the database
collections = test_db.list_collection_names()
