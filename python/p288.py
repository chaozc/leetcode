class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.dic = {}
        for it in dictionary:
            if len(it) > 2:
                if not self.dic.has_key(it[0]+str(len(it)-2)+it[-1]):
                    self.dic[it[0]+str(len(it)-2)+it[-1]] = []
                self.dic[it[0]+str(len(it)-2)+it[-1]].append(it)
            else:
                if not self.dic.has_key(it):
                    self.dic[it] = []
                self.dic[it].append(it)
        

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        if len(word) > 2:
            abb = word[0]+str(len(word)-2)+word[-1]
        else:
            abb = word
        if self.dic.has_key(abb) == False:
            return True
        else:
            for w in self.dic[abb]:
                if w != word:
                    return False
            return True


# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")