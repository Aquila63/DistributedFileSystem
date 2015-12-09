from collections import deque

class Cache:

    CACHE_MAX_SIZE = 10
    cache = {}
    keys = deque()

    def __init__(self):
        pass

    def search(self, key):
        if key in self.cache:
            return True
        else:
            return False

    def purge_entry(self):
        key = keys.popleft()
        self.remove(key)

    def remove(self, key):
        del self.cache[key]
        print "{0} removed from cache".format(key)

    def add(self, key, value):
        if len(self.keys) == self.CACHE_MAX_SIZE:
            purge_entry()

        self.cache[key] = value
        print "{0} added to the cache".format(key)

    def retrieve(self, key):
        #if self.search_cache(key):
        return self.cache[key]
        #else
        #    return -1
