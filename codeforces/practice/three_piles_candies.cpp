#include <bits/stdc++.h>
using namespace std;

int main() {
    int q;
    cin >> q;
    for (int t = 0; t < q; t++) {
        long piles[3];
        cin >> piles[0] >> piles[1] >> piles[2];

        long minDiff = INFINITY;
        int x, y = 0;
        for (int i = 0; i < 3; i++) {
            for (int j = i; j < 3; j++) {
                if (i == j)
                    continue;

                long diff = labs(piles[i] - piles[j]);
                if (diff < minDiff) {
                    minDiff = diff;
                    x = i;
                    y = j;
                }
            }
        }

        long alice = max(piles[x], piles[y]);
        long bob = min(piles[x], piles[y]);
        long share = piles[0] + piles[1] + piles[2] - piles[x] - piles[y];
        if (minDiff >= share) {
            cout << alice << endl;
        } else {
            share -= minDiff;
            bob = alice;
            alice += share / 2;
            cout << alice << endl;
        }
    }
}
