#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        long a, b;
        cin >> a >> b;

        if (a % b == 0) {
            cout << 0 << endl;
            continue;
        }

        long ans = (((a / b) + 1) * b) - a;
        cout << ans << endl;
    }
}
