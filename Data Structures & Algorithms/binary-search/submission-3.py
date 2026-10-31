class Solution:
    def search(self, nums: List[int], target: int) -> int:
        high = len(nums) - 1
        low = 0
        return self.binary_search(nums, low, high, target)
    def binary_search(self, arr, low, high, target):
        if low > high:
            return -1
        mid = low + (high - low) // 2 
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return self.binary_search(arr, low, mid - 1, target)
        else:
            return self.binary_search(arr, mid + 1, high, target)
