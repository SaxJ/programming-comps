#include <bits/stdc++.h>
using namespace std;

// covid range = 2

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int N;
        cin >> N;
        int distances[N];
        int last = -1;
        int minConnected;
        int maxConnected;
        minConnected = 200;
        maxConnected = 0;

        int count = 0;
        for (int i = 0; i < N; i++) {
            int current;
            cin >> current;

            if (last < 0) {
                count++;
            } else {
                int diff = current - last;
                if (diff <= 2) {
                    count++;
                } else {
                    minConnected = min(count, minConnected);
                    maxConnected = max(count, maxConnected);
                    count = 1;
                }
            }

            last = current;
        }

        minConnected = min(count, minConnected);
        maxConnected = max(count, maxConnected);
        cout << minConnected << " " << maxConnected << endl;
    }
}
