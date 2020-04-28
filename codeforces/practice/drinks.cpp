#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    int total = 0;
    for (int i = 0; i < n; i++) {
        int p;
        cin >> p;
        total += p;
    }
    double ans = (double)total / n;
    cout << ans << endl;
}
