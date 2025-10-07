class Solution(object):
    def romanToInt(self, s):
        symbList = {
            "I": 1,   "V": 5,
            "X": 10,  "L": 50,
            "C": 100, "D": 500,
            "M": 1000
        }

        return self.findNumber(s, symbList)

    def findNumber(self, s, symbList):
        lastSymb = ""
        number = 0

        for symb in s:
            if lastSymb and symbList[lastSymb] < symbList[symb]:
                number += symbList[symb] - 2 * symbList[lastSymb]
            else:
                number += symbList[symb]

            lastSymb = symb
        
        return number
