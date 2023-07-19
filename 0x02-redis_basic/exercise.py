#!/usr/bin/env python3
"""
creating a cache class in the init method
"""
from typing import Union, Callable
import redis
import uuid
import functools


def count_calls(method):
    """count calls decorator taking a single callable"""
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """the wrapper function"""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """
    the cache class
    """
    def __init__(self):
        """the init method storing an instance of redis client(private)"""
        self._redis = redis.Redis()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        a store method that takes data arg and returns a str.
        the method generates a random key, stores the input data
        in redis using te random key
        """
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int]:
        """get method takes in a key str witn optiona callable"""
        data = self._redis.get(key)
        if data is None:
            return None

        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Union[str, None]:
        """get str auto parameterizes cache.get with correct conversion"""
        return self._redis.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Union[int, None]:
        """get int auto parameterizes caceh.get with correct conversion"""
        return self._redis.get(key, fn=int)

    def flush(self):
        """flushing the redis instance"""
        self._redis.flushdb()
