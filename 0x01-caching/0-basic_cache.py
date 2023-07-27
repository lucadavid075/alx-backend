#!/usr/bin/env python3
"""
Basic dictionary.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    A class that represents a caching system that allows
    storing and retrieving items from a dictionary.
    """
    def put(self, key, item):
        """
        Method that adds an item in the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Method that retrieves an item by key.
        """
        return self.cache_data.get(key, None)
