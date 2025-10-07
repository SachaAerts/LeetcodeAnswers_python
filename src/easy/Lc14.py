class Solution(object):
    def longestCommonPrefix(self, strs):
        longerWord = max(strs, key=len)
        actualPrefix = ""

        if self.hasOneWord(strs):
            return strs[0]

        return self.browseWords(strs, longerWord, actualPrefix)

    def browseWords(self, strs, longerWord, actualPrefix):
        for index, value in enumerate(longerWord):
            for j in range(index, len(longerWord)):
                actualPrefix += longerWord[j]
                if not self.isPrefixIn(strs, actualPrefix):
                    return actualPrefix[:-1]

        return actualPrefix

    def hasOneWord(self, strs):
        return len(strs) == 1

    def isPrefixIn(self, strs, actualPrefix):
        for word in strs:
            if not word.startswith(actualPrefix, 0):
                return False
        return True


            
        
        
