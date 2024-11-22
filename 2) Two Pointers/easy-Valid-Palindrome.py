class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while (l < r):
            if s[l].isalnum() and s[r].isalnum():
                if s[l].casefold() != s[r].casefold():
                    return False
                r -= 1
                l += 1
            else:
                if not s[l].isalnum():
                    l += 1
                if not s[r].isalnum():
                    r -= 1

        return True
