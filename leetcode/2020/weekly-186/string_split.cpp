#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxScore(string s) {
        int zeros = 0;
        int right = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '1')
                right++;
        }

        int ans = 0;
        int left = 0;
        for (int i = 0; i < s.length() - 1; i++) {
            char c = s[i];
            if (c == '1')
                right--;
            else
                left++;
            ans = max(left + right, ans);
        }

        return ans;
    }
};
