#!/usr/bin/env python3
"""
Redis module, Writing strings to Redis
Reading from Redis and recovering original type
Incrementing values, storing lists, Retrieving lists
"""

import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    """
    Store an instance of the Redis client as a private variable named _redis
    Flush the instance using flushdb
    """

    def __init__(self):
        """Prototype: def __init__(self):
        Store instance of Redis client as private variable _redis
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store history of inputs and outputs for a particular function
        """
        gen = str(uuid.uuid4())
        self._redis.set(gen, data)
        return gen

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """
        Convert data back to desired format
        """
        data = self._redis.get(key)
        return fn(data) if fn else data

    def get_int(self, data):
        """
        Convert data to int
        """
        return self.get(data, int)

    def get_str(self, key):
        """
        Convert data to str
        """
        data = self.get(key)
        return data.decode('utf-8')
