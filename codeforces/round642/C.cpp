#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    cin >> T;

    map<unsigned long long, unsigned long long> squares;
    squares.insert(make_pair(1, 0));
    squares.insert(make_pair(3, 8));

    unsigned long long maxN = 1;
    for (int t = 0; t < T; t++) {
        unsigned long long n;
        cin >> n;
        if (n > maxN) {
            for (int i = maxN + 2; i <= n; i += 2) {
                unsigned long long outer = i + (2 * (i - 1)) + (i - 2);
                unsigned long long level = i / 2;
                unsigned long long layer = outer * level;
                squares.insert(make_pair(i, layer + squares.at(i - 2)));
            }
            maxN = n;
        }

        unsigned long long total = squares.at(n);
        cout << total << endl;
    }
}
