class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = nums[0]
        high = total
        for i in range(len(nums) - 1):
            if nums[i+1] > total + nums[i+1]:
                total = nums[i+1]
            else:
                total += nums[i+1]
            high = max(high, total)
        return high
            
