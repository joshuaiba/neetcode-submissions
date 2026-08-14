import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = dict()

        for num in nums:
            seen[num] = seen.get(num,0) + 1
        
        heap = []
        for key in seen.keys():
            heapq.heappush(heap, (seen[key], key))
            if len(heap) > k:
                heapq.heappop(heap)
        
        top = []
        for i in range(k):
            top.append(heapq.heappop(heap)[1])

        return top