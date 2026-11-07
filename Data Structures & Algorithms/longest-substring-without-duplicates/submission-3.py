class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        high = 0
        l = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            high = max(high, len(seen))
        return high
