#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    cin >> T;

    for (int t = 0; t < T; t++) {
        int n, k;
        cin >> n >> k;

        int as[n];
        int bs[n];
        for (int i = 0; i < n; i++)
            cin >> as[i];
        for (int i = 0; i < n; i++)
            cin >> bs[i];

        sort(as, as + n);
        sort(bs, bs + n, greater<int>());
        for (int i = 0; i < k; i++) {
            if (as[i] > bs[i])
                break;
            else
                as[i] = bs[i];
        }
        int total = 0;
        for (int i = 0; i < n; i++)
            total += as[i];
        cout << total << endl;
    }
}
