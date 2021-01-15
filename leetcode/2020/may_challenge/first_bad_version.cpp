#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int firstBadVersion(int n) {
        long long lower = 1;
        long long upper = n;
        while (lower < upper) {
            long long mid = (lower + upper) / 2;
            if (isBadVersion(mid))
                upper = mid;
            else
                lower = mid + 1;
        }
        return upper;
    }
};
