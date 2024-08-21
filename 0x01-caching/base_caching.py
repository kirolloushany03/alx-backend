#!/usr/bin/env python3
"""basic cashing dictionary"""
from base_caching import BaseCaching

class BasicCache(BaseCaching):
    def put(self, key, item):
        """Add key-value pair to cache if neither is None."""
        if key is not None and item is not None:
            self.cache_data[key]= item
    
    def get(self, key):
        """Retrieve value from cache linked to key, or return None."""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None