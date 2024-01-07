class Solution {
public:
    bool isSubsequence(string str1, string str2) {
        int j = 0;
        for (int i = 0; i < str2.length() && j < str1.length(); i++) {
            if (str1[j] == str2[i]) {
                j++;
        }
    }
    return (j == str1.length());
    }
};