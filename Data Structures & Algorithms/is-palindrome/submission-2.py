class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped = ""
        for c in s:
            if (c.isalnum()):
                stripped += c
        stripped = stripped.lower()
        if (stripped == stripped[::-1]):
            return True
        else:
            return False