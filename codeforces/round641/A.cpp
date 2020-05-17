#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int n, k;
        cin >> n >> k;
        for (int i = 0; i < k; i++) {
            if (n % 2 == 0) {
                n = n + 2 * (k - i);
                break;
            } else {
                int i = 3;
                while (true) {
                    if (n % i == 0) {
                        n += i;
                        break;
                    }
                    i += 2;
                }
            }
        }
        cout << n << endl;
    }
}

