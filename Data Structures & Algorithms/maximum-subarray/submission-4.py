class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = nums[0]
        high = total
        for i in range(1, len(nums)):
            if nums[i] > total + nums[i]:
                total = nums[i]
            else:
                total += nums[i]
            high = max(high, total)
        return high
            
