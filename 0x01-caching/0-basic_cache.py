#!/usr/bin/env python3
"""basic cashing dictionary"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Represents an object that allows storing and
    retrieving items from a dictionary.
    """
    def put(self, key, item):
        """
        Add key-value pair to cache if neither is None
        """
        if key is None and item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve value from cache linked to key, or return None
        """
        return self.cache_data.get(key, None)
