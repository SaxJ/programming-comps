#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int n;
        cin >> n;
        int candies[n];
        for (int i = 0; i < n; i++)
            cin >> candies[i];

        int ai = 0;
        int bi = n - 1;
        int a, b;
        int last = 0;
        a = b = 0;
        int moves = 0;
        bool done = false;
        while (bi > ai && !done) {
            int eaten = 0;
            if (moves % 2 == 0) {
                int d = 0;
                while (eaten < last) {
                    if (ai + d >= bi) {
                        done = true;
                        break;
                    }

                    eaten += candies[ai + d];
                    d++;
                }
                if (!done) {
                    ai += d;
                    a += eaten;
                }
            } else {
                int d = 0;
                while (eaten < last) {
                    if (bi - d <= bi) {
                        done = true;
                        break;
                    }

                    eaten += candies[bi - d];
                    d++;
                }
                if (!done) {
                    bi -= d;
                    b += eaten;
                }
            }
            if (!done) {
                moves++;
                last = eaten;
            }
        }
        cout << moves << " " << a << " " << b << endl;
    }
}

