class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        cond = False
        for i in range(len(matrix)):
            if self.binarySearch(matrix[i], 0, len(matrix[i]) - 1, target) == target:
                cond = True
        return cond

    def binarySearch(self, arr, low, high, target):
        if low > high:
            return -1
        mid = low + (high - low) // 2
        if arr[mid] > target:
            return self.binarySearch(arr, low, mid - 1, target)
        elif arr[mid] < target:
            return self.binarySearch(arr, mid + 1, high, target)
        else:
            return target