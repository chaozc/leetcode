class Node:
    def __init__(self):
        self.abc = [None for i in range(26)]
        self.end = False
class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = Node() 

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for c in word:
            id = ord(c)-ord('a')
            if node.abc[id] == None:
                node.abc[id] = Node()
            node = node.abc[id]
        node.end = True
    def dfs(self, word, node):
        if word == '':
            return node.end
        if word[0] == '.':
            for i in range(26):
                if node.abc[i] and self.dfs(word[1:], node.abc[i]):
                    return True
            return False
        else:
            if node.abc[ord(word[0])-ord('a')] and self.dfs(word[1:], node.abc[ord(word[0])-ord('a')]):
                return True
            else:
                return False
    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.dfs(word, self.root)
# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")