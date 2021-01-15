class Solution:
    croaks = {}

    def before(self, c):
        word = "croak"
        if c not in word or c == "c":
            return None
        return word[word.index(c) - 1]

    def add(self, c):
        if c not in self.croaks:
            self.croaks[c] = 0
        self.croaks[c] += 1

    def minNumberOfFrogs(self, croakOfFrogs):  # str -> int
        self.croaks = {}
        frogs = 0
        maxFrogs = 0
        for c in croakOfFrogs:
            b = self.before(c)
            if b is None:
                if c == "c":
                    frogs += 1
                    maxFrogs = frogs if frogs > maxFrogs else maxFrogs
                    self.add(c)
                else:
                    return -1
            else:
                if b not in self.croaks or self.croaks[b] == 0:
                    return -1
                else:
                    self.croaks[b] -= 1
                    self.add(c)
                    if c == "k":
                        frogs -= 1

        for k in self.croaks:
            if self.croaks[k] > 0 and k != "k":
                return -1
        return maxFrogs


s = Solution()
print(s.minNumberOfFrogs("crocracokrakoak"))
