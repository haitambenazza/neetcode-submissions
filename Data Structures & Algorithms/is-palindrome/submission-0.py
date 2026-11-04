class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not len(s):
            return True
        new: str = ''
        for c in s:
            if c.isdigit() or c.isalpha():
                new += new.join(c.upper())
        last = len(new) - 1
        for i in new:
            if i != new[last]:
                return False
            last -= 1
        return True
            
        