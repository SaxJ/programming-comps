#include <bits/stdc++.h>
using namespace std;

int lcm(int a, int b) {
    return (a * b) / __gcd(a, b);
}

int main() {
    int n;
    cin >> n;
    int ans;
    cin >> ans;
    int ans2 = ans;

    for (int i = 1; i < n; i++) {
        int x;
        cin >> x;
        ans = __gcd(ans, x);
        ans2 = lcm(ans2, x);
    }

    cout << ans << endl;
    cout << ans2 << endl;
}
