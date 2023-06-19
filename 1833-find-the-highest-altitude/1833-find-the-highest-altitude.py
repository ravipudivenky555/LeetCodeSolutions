class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        currAlt=maxAlt=0
        for i in gain:
            currAlt+=i
            maxAlt=max(maxAlt,currAlt)
        return maxAlt