#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int numJewelsInStones(string J, string S) {
        set<char> jewels;
        for (char& c : J)
            jewels.insert(c);

        int count = 0;
        for (char& c : S) {
            if (jewels.find(c) == jewels.end())
                continue;
            else
                count++;
        }
        return count;
    }
};
