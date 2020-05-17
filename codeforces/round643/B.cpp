#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int n;
        cin >> n;

        vector<int> es;
        for (int i = 0; i < n; i++) {
            int x;
            cin >> x;
            es.push_back(x);
        }

        sort(es.begin(), es.end(), greater<int>());
        int groups = 0;
        int p = 0;
        while (p < n) {
            int e = es[p];
            p += e;
            if (p <= n)
                groups++;
        }

        cout << groups << endl;
    }
}
