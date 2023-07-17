#!/usr/bin/env python3
"""
a function to list all documents in a collection
"""


def list_all(mongo_collection):
    """lists all the documents in the collection"""
    documents = []

    for doc in mongo_collection.find():
        document.append(doc)

    return documents
