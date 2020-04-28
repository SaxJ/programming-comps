#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int a, b;
        cin >> a >> b;
        int diff = b - a;
        if (diff == 0)
            cout << 0 << endl;
        else if (diff > 0) {
            if (diff % 2 == 0)
                cout << 2 << endl;
            else
                cout << 1 << endl;
        } else {
            diff = abs(diff);
            if (diff % 2 == 0)
                cout << 1 << endl;
            else
                cout << 2 << endl;
        }
    }
}
