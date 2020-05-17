#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    cin >> T;

    for (int t = 0; t < T; t++) {
        int n, m;
        cin >> n >> m;

        if (n == 1)
            cout << 0 << endl;
        else if (n == 2)
            cout << m << endl;
        else
            cout << 2 * m << endl;
    }
}
