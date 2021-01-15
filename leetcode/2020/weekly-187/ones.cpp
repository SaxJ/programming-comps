#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool kLengthApart(vector<int>& nums, int k) {
        int last = -(k + 1);
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == 1) {
                long diff = i - last;
                if (diff <= k)
                    return false;
                last = i;
            }
        }

        return true;
    }
};
