class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> arr;
        unordered_map<string, vector<string>> seen;
        for (auto s : strs) {
            string temp = s;
            sort(temp.begin(), temp.end());
            if (!seen.contains(temp)) {
                seen[temp].push_back(s);
            } else if (seen.contains(temp)) {
                seen[temp].push_back(s);
            }
        }
        for (auto s : strs) {
            string temp = s;
            sort(temp.begin(), temp.end());
            if (find(arr.begin(), arr.end(), seen[temp]) == arr.end()) {
                arr.push_back(seen[temp]);
            }
        }
        

        return arr;
    }
};