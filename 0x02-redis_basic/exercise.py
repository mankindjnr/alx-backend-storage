#!/usr/bin/env python3
"""
creating a cache class in the init method
"""
from typing import Union, Callable, Any
import redis
import uuid
import functools


def replay(method: Callable) -> None:
    """display the history of calls of a particular func"""
    imputs_key = f"{method.__qualname__}:inputs"
    outputs_key = f"{method.__qualname__}:outputs"

    inputs = cache._redis.lrange(inputs_key, 0, -1)
    outputs = cache._redis.lrange(outputs, 0, -1)

    print(f"{method.__qualname__} was called {len(inputs)} times:")

    for ins, outs in zip(inputs, outputs):
        print(f"{method.__qualname__}(*{ins.decode()}) -> {outs.decode()}")


def call_history(method: Callable) -> Callable:
    """redis commands rpush, lpush, lrange"""
    @functools.wraps(method)
    def wrapper(self, *args: Any, **kwargs: Any) -> Any:
        """the wrapper for call history"""
        inputs_key = f"{method.__qualname__}:inputs"
        outputs_key = f"{method.__qualname__}:outputs"

        self._redis.rpush(inputs_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(outputs_key, output)

        return output
    return wrapper


def count_calls(method: Callable) -> Callable:
    """count calls decorator taking a single callable"""
    @functools.wraps(method)
    def wrapper(self, *args: Any, **kwargs: Any) -> Any:
        """the wrapper function"""
        key: str = method.__qualname__
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
    @call_history
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
