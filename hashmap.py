import random

class HMap(object):

    def __init__(self):

        self.map = {}
        self.keys = []
        self.length = 0

    def insert(self, key, value):
        index = self.length
        self.map[key] = (value, index)
        self.keys.append(key)
        self.length += 1

    def get(self, key):
        return self.map[key][0]

    def delete(self, key):
        index = self.map[key][1]
        self.keys[index] = self.keys[self.length - 1]
        self.keys.pop()
        self.length -= 1

        del self.map[key]
        self.map[self.keys[index]] = (self.map[self.keys[index]][0], index)

    def random_key(self):
        return random.choice(self.keys)