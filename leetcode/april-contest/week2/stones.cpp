#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        make_heap(stones.begin(), stones.end());
        while (stones.size() > 1) {
            int y = stones.front();
            pop_heap(stones.begin(), stones.end());
            stones.pop_back();

            int x = stones.front();
            pop_heap(stones.begin(), stones.end());
            stones.pop_back();

            if (x == y)
                continue;
            stones.push_back(y - x);
            push_heap(stones.begin(), stones.end());
        }

        return stones.empty() ? 0 : stones.front();
    }
};

int main() {
    vector<int> a;
    for (int i = 1; i < 10; i++)
       a.push_back(i);
    Solution s;
    int ans = s.lastStoneWeight(a);
}
