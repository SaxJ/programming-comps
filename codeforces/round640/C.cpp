#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        long long n, k;
        cin >> n >> k;

        long long r = k % n;
        long long ans = (n * ceil((float)k / n)) + r;
        cout << ans << endl;
    }
}
