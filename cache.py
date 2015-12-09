from collections import deque

class Cache:

    CACHE_MAX_SIZE = 5

    #Cache is implemented as a dict
    #Key = Filename
    #Value = Data
    cache = {}

    #Used deque as it allows me to pop a list from the left, i.e. the oldest key
    #in the cache will be purged, and the other elements are shifted left.
    keys = deque()

    def __init__(self):
        pass

    #Seach for a key in the cache
    def search(self, key):
        if key in self.cache:
            return True
        else:
            return False

    #Delete the oldest entry in the cache
    def purge_entry(self):
        key = keys.popleft()
        self.remove(key)

    #Remove a given key/file from the cache
    def remove(self, key):
        del self.cache[key]
        print "{0} removed from cache".format(key)

    #Add a key and value to the cache
    def add(self, key, value):
        #Check if the cache is full
        if len(self.keys) == self.CACHE_MAX_SIZE:
            purge_entry()

        self.cache[key] = value
        print "{0} added to the cache".format(key)

    #Retrieve an element from the cache
    def retrieve(self, key):
        #if self.search_cache(key):
        return self.cache[key]
        #else
        #    return -1
