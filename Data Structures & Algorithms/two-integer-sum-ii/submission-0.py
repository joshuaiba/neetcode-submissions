class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = dict()
        for i, num in enumerate(numbers):
            r = target - num
            if r in seen:
                return [seen[r]+1, i+1]
            else:
                seen[num] = i