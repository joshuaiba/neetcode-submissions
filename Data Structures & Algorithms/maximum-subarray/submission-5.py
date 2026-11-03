class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = nums[0]
        high = total
        for i in range(1, len(nums)):
            total = max(nums[i], nums[i] + total)
            high = max(high, total)
        return high
            
