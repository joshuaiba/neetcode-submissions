import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        sets = []
        for num, c in count.items():
            sets.append([c, num])
        sets.sort()

        freq = []
        for i in range(k):
            freq.append(sets.pop()[1])
        return freq

        