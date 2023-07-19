#!/usr/bin/env python3
"""
we have 3 hats, each hat is held in a redis hash of field-value pairs,
and the hash has a key that is a prefixed random integer,i.e hat:567898976
using the hat:prefix, is redis convention for creating a sort of namespace within a redis database
"""
import random

random.seed(444)
hats = {f"hat:{random.getrandbits(32)}": i for i in (
    {
        "color": "black",
        "price": 49.99,
        "style": "fitted",
        "quantity": 1000,
        "npurchased": 0,
    },
    {
        "color": "maroon",
        "price": 59.99,
        "style": "hipster",
        "quantity": 500,
        "npurchased": 0,
    },
    {
        "color": "green",
        "price": 99.99,
        "style": "baseball",
        "quantity": 200,
        "npurchased": 0,
    })
}

"""
we will start with datbase 1
"""
import redis
import pprint

r = redis.Redis(db=1)

"""
to do an initial write of this data into REDIS, we can use .hmset() (hash multi-set)
we will call it for each disctionary. the multi is a reference to setting multiple field-value pairs
where field corresponds to a key of any of the nested dictionaries in hats.
"""
with r.pipeline() as pipe:
    for h_id, hat in hats.items():
        pipe.hmset(h_id, hat)
    pipe.execute()

print(r.bgsave())
print(r.hgetall("hat:56854717"))
print(r.keys())