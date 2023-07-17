#!/usr/bin/env python3
"""
a function to list all documents in a collection
"""


def list_all(mongo_collection):
    """lists all the documents in the collection"""
    collections = list(mongo_collection.find())
    return collections

if __name__ == "__main__":
    list_all(mongo_collection)
