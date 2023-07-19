#!/usr/bin/env python3
"""
creating a cache class in the init method
"""
from typing import Union
import redis
import uuid


class Cache:
    """
    the cache class
    """
    def __init__(self):
        """the init method storing an instance of redis client(private)"""
        self._redis = redis.Redis()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        a store method that takes data arg and returns a str.
        the method generates a random key, stores the input data
        in redis using te random key
        """
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def flush(self):
        """flushing the redis instance"""
        self._redis.flushdb()
