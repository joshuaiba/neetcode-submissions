class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int left = 0;
        int right = numbers.size() - 1;
        while((numbers[left] + numbers[right]) != target) {
            if ((numbers[left] + numbers[right]) < target) {
                left += 1;
            } else {
                right -= 1;
            }
        }
        return {left + 1, right + 1};
    }
};
