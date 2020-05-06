#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int longestSubarray(vector<int>& nums, int limit) {
        if (nums.size() < 2)
            return 0;

        int lower = 0;
        int upper = 1;
        int small = nums[0];
        int si = 0;
        int large = nums[0];
        int longest = 0;
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] < small
            small = min(small, nums[i]);
            large = max(large, nums[i]);

            if (large - small <= limit)
                longest = max(longest, i - lower + 1);
            else {
                lower++;
                
                small = large = nums[i];
            }
        }

        return longest;
    }
};
