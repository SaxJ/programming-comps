#include <bits/stdc++.h>
using namespace std;

bool isSquare(long x) {
    long double sr = sqrt(x);
    return ((sr - floor(sr)) == 0);
}

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int n;
        cin >> n;

        long total = 0;
        vector<int> prefixes;
        prefixes.push_back(0);

        for (int i = 0; i < n; i++) {
            int x;
            cin >> x;

            total += x;
            prefixes.push_back(total);
        }

        int count = 0;
        for (int i = 1; i < prefixes.size(); i++) {
            for (int j = 0; j < i; j++) {
                long subarray = prefixes[i] - prefixes[j];
                if (isSquare(subarray))
                    count++;
            }
        }

        cout << "Case #" << (t + 1) << ": " << count << endl;
    }
}
