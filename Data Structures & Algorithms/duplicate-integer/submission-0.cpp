class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int, int> seen;
        for (int i : nums) {
            if (!seen[i]) {
                seen[i] = 1;
            } else if (seen[i] == 1) {
                return true;
            }
        }
        return false;
    }
};