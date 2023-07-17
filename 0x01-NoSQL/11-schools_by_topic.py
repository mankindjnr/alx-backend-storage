#!/usr/bin/env python3
"""
retrieve docs by topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    returns the list of school having a specific topic
    """
    schools = mongo_collection.find({"topics": topic})
    return [school for school in schools]
