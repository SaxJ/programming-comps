#include <bits/stdc++.h>

using namespace std;

int main() {
    int q;
    cin >> q;
    for (int i = 0; i < q; i++) {
        long long n;
        cin >> n;
        if (n < 4)
            cout << (4 - n) << endl;
        else
            cout << ((n % 2 == 0) ? 0 : 1) << endl;
    }
}
