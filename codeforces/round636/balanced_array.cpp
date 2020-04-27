#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int n;
        cin >> n;
        int half = n / 2;
        if (half % 2 != 0)
            cout << "NO" << endl;
        else {
            cout << "YES" << endl;
            int evenSum = 0;
            for (int i = 2; i <= n; i += 2) {
                cout << i << " ";
                evenSum += i;
            }

            int oddSum = 0;
            for (int i = 1; i < n - 1; i += 2) {
                cout << i << " ";
                oddSum += i;
            }

            cout << (evenSum - oddSum) << endl;
        }
    }
}

