#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int n, a, b, c, d;
        cin >> n >> a >> b >> c >> d;
        int minWeight = (a - b) * n;
        int maxWeight = (a + b) * n;
        int minBag = c - d;
        int maxBag = c + d;

        if (minWeight > maxBag || maxWeight < minBag)
            cout << "NO" << endl;
        else
            cout << "YES" << endl;
    }
}
