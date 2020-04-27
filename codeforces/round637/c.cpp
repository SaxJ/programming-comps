#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int n;
        cin >> n;

        int nums[n + 1];
        vector<pair<int, int>> pairs;
        for (int i = 0; i < n; i++) {
            int x;
            cin >> x;
            nums[i + 1] = x;
            pairs.push_back(make_pair(x, i + 1));
        }
        sort(pairs.begin(), pairs.end());
        // too tired now
