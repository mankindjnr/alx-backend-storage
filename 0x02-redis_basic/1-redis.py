#!/usr/bin/env python3
import redis
import datetime

r =redis.Redis()

today = datetime.date.today()
today = today.isoformat()
print(today)
visitors = {"dan", "jon", "alex"}
print(r.sadd(today, *visitors))
print(r.smembers(today))
#print(r.scard(today.isoformat()))

""" 
this will result to an error due to the invalid format.
you'll need to explicitly convert the python date object to str .isoformat():

r.sadd(today, *visitors)
"""
