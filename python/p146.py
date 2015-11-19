class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.pre = None

class DDL:
    def __init__(self):
        self.h = None
        self.t = None
        
    def insertAtFirst(self, node):
        if self.t == None:
            self.h = node
            self.t = node
        else:
            node.next = self.h
            self.h.pre = node
            self.h = node
    def remove(self, node):
        if self.h == node and self.t == node:
            self.h, self.t = None, None
        elif self.h == node:
            self.h = node.next
        elif self.t == node:
            self.t = node.pre
        else:
            node.pre.next = node.next
            node.next.pre = node.pre
    def removeLast(self):
        self.remove(self.t)
        
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.cache = {}
        self.ddl = DDL()
        self.size = 0

    def get(self, key):
        """
        :rtype: int
        """
        if not self.cache.has_key(key):
            return -1
        self.ddl.remove(self.cache[key])
        self.ddl.insertAtFirst(self.cache[key])
        return self.cache[key].val
    def isFull(self):
        return self.cap == self.size
    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if self.isFull() and (not self.cache.has_key(key)):
            del self.cache[self.ddl.t.key]
            self.ddl.removeLast()
            self.cache[key] = Node(key, value)
            self.ddl.insertAtFirst(self.cache[key])
        elif (not self.cache.has_key(key)):
            self.cache[key] = Node(key, value)
            self.ddl.insertAtFirst(self.cache[key])
            self.size += 1
        else:
            self.cache[key].val = value
            self.ddl.remove(self.cache[key])
            self.ddl.insertAtFirst(self.cache[key])