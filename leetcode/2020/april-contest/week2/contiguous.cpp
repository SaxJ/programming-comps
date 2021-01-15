#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        long accum[nums.size()];

        long total = 0;
        for (int i = 0; i < nums.size(); i++) {
            total += (nums[i] == 0) ? -1 : 1;
            accum[i] = total;
        }

        map<int, int> firstOccurrance;
        firstOccurrance.insert(make_pair(0, -1));
        int maxDiff = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (firstOccurrance.find(accum[i]) == firstOccurrance.end())
                firstOccurrance.insert(make_pair(accum[i], i));
            else {
                int diff = i - firstOccurrance.find(accum[i])->second;
                maxDiff = max(diff, maxDiff);
            }
        }

        return maxDiff;
    }
};
