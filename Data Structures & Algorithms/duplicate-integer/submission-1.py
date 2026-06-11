class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = dict()
        for i, num in enumerate(nums):
            if num not in seen:
                seen[num] = 1
            else:
                return True
        return False