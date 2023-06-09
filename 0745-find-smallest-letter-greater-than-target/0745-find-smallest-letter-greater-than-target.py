from string import ascii_lowercase
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target>=max(letters):return letters[0]
        l=set(letters)
        for i in ascii_lowercase:
            if i<=target and i in l:
                l.remove(i)
        return min(l)