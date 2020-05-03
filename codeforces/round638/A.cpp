#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int n;
        cin >> n;

        long long a = 0;
        long long b = 0;
        for (int i = 0; i < n; i++) {
            if (i % 2 == 0)
                a += pow(2, i + 1);
            else
                b += pow(2, i + 1);
        }
        cout << labs(a - b) << endl;
    }
}
