#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin >> t;
    for (int ti = 0; ti < t; ti++) {
        int n, m;
        cin >> n >> m;

        if (n == 1 || m == 1 || (n == 2 && m == 2))
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }
}

