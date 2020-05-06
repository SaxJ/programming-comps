#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    cin >> T;
    map<int, long> heights;
    heights.insert(make_pair(1, 2));
    int maxHeight = 1;
    for (int t = 0; t < T; t++) {
        int n;
        cin >> n;
        int towers = 0;
        
        while (n >= 2) {
            towers++;
            long diff = 5;
            int height = 1;
            long cards = 2;
            while (cards < n) {
                long next = cards + diff;
                if (next > n)
                    break;
                cards += diff;
                diff += 3;
                height++;
            }
            n -= cards;
        }
        cout << towers << endl;
    }
}

