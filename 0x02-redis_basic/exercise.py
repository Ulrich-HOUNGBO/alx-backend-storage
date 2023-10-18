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

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Prototype: def store(self, data: Union[str, bytes, int, float])
        Generates a random key (e.g. using uuid)
        Stores the input data in Redis using the random key
        Returns the key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
