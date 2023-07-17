#!/usr/bin/env python3
"""
inserts a new documnet in a collection
"""


def insert_school(mongo_collection, **kwargs):
    """insert new doc in  collection based on kwargs"""
    _id = mongo_collection.insert_one(kwargs).inserted_id

    return _id
