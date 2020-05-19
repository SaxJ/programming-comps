#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    cin >> T;

    for (int t = 0; t < T; t++) {
        int n, k;
        cin >> n >> k;

        bool inProgress = false;
        int count = 0;
        int last = -1;
        for (int i = 0; i < n; i++) {
            int a;
            cin >> a;

            if (a == k) {
                inProgress = true;
                last = a;
                continue;
            }

            if (inProgress && last != (a + 1)) {
                inProgress = false;
                last = a;
                continue;
            }

            if (inProgress && a == 1) {
                count++;
                inProgress = false;
                last = a;
                continue;
            }

            last = a;
        }
        cout << "Case #" << (t + 1) << ": " << count << endl;
    }
}
