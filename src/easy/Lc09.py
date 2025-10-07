class Solution(object):
    def verifInverse(self, numberString):
        verifString = ""
        for i in reversed(numberString):
            verifString += i
        
        return verifString

    def isPalindrome(self, x):
        return str(x) == self.verifInverse(str(x))
        
