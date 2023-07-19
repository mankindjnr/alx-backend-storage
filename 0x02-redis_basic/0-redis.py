#!/usr/bin/env python3
import redis

"""
this is where we will call and execute almost any redis command
we will call redis commands using methods on the class instance
    r
    =the redis instance

below: that instance has been built with no args
"""
r = redis.Redis()
r.mset({"Kenya": "Nairobi", "Roysambu": "Githurai"})

"""
without the decode, the trype of the return type is of byte
with the decode, it returns a value of type string
"""
print(type(r.get("Kenya").decode("utf-8")))
