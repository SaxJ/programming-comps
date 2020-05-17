#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    cin >> T;

    for (int t = 0; t < T; t++) {
        int n;
        cin >> n;
        long sizes[n];

        for (int i = 0; i < n; i++)
            cin >> sizes[i];

        stack<pair<int, long>> stk;
        while (stk.size() > 0) {
            auto current = stk.top();
            stk.pop();

        }
    }
}
