class Solution(object):
    def lengthOfLongestSubstring(self, s):
        currentSerie = ""
        maxSerie = ""

        for charac in s:
            if charac in currentSerie:
                if len(currentSerie) > len(maxSerie):
                    maxSerie = currentSerie
                cut = currentSerie.index(charac) + 1
                currentSerie = currentSerie[cut:] + charac
            else:
                currentSerie += charac

        if len(currentSerie) > len(maxSerie):
            maxSerie = currentSerie

        return len(maxSerie)
