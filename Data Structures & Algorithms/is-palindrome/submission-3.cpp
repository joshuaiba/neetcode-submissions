class Solution {
public:
    bool isPalindrome(string s) {
        string stripped = "";
        for (char c : s) {
            if (isalnum(c)) {
                stripped.push_back(tolower(c));
            }
        }
        string t = stripped;
        reverse(t.begin(), t.end());
        if (stripped == t) {
            return true;
        }
        return false;
    }
};
