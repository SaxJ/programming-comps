#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int firstUniqChar(string s) {
        map<char, vector<int>> seen;
        for (int i = 0; i < s.length(); i++) {
            char c = s[i];
            if (seen.find(c) == seen.end())
                seen.insert(make_pair(c, vector<int>({i})));
            else
                seen.at(c).push_back(i);
        }

        int minIndex = s.length();
        for (auto it : seen) {
            if (it.second.size() == 1)
                minIndex = min(minIndex, it.second[0]);
        }
        return minIndex == s.length() ? -1 : minIndex;
    }
};
