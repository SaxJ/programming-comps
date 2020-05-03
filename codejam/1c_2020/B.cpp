#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int u;
        cin >> u;

        map<char, set<int>> possible;
        for (int i = 0; i < 10000; i++) {
            long long q;
            cin >> q;
            string r;
            cin >> r;
            
            if (q < 0)
                continue;
            else {
                for (char& c : r) {
                    set<int> newSet;
                    possible.insert(make_pair(c, newSet));
                }
            }
        }
    }
}
