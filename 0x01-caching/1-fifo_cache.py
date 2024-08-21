#!/usr/bin/env python3
"""FIFO caching"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """A FIFO caching system that inherits from BaseCaching"""

    def __init__(self):
        """Initialize the cache with the parent class's initialization"""
        super().__init__()

    def put(self, key, item):
        """Add an item to the cache,
        removing the oldest if cache exceeds max size"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_item = next(iter(self.cache_data))
                print(f"DISCARD: {first_item}")
                self.cache_data.pop(first_item)

    def get(self, key):
        """Retrieve an item from the cache by key,
        returning None if key doesn't exist
        """
        return self.cache_data.get(key, None)
