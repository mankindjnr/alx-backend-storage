#!/usr/bin/env python3
"""
changes all topics of a school doc based on the name
"""


def update_topics(mongo_collection, name, topics):
    """
    function changes all topics of a school doc based on name
    """
    mongo_collection.update_one({"name": name}, {"$set": {"topics": topics}})
