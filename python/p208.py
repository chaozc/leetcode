class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.next = [None for i in range(26)]
        self.end = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for c in word:
            if node.next[ord(c)-ord('a')] == None:
                node.next[ord(c)-ord('a')] = TrieNode()
            node = node.next[ord(c)-ord('a')]
        node.end = True
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for c in word:
            if node.next[ord(c)-ord('a')] == None:
                return False
            node = node.next[ord(c)-ord('a')]
        if node.end:
            return True
        else:
            return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for c in prefix:
            if node.next[ord(c)-ord('a')] == None:
                return False
            node = node.next[ord(c)-ord('a')]
        return True

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")