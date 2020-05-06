#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int n;
        cin >> n;
        long arr[n];
        int occupation[2 * n];
        for (int i = 0; i < n; i++)
            cin >> arr[i];

        set<long> seen;
        bool collision = false;
        for (int i = 0; i < 2 * n; i++) {
            long newRoom = i + arr[i % n];
            if (seen.find(newRoom) != seen.end()) {
                collision = true;
                break;
            }
            seen.insert(newRoom);
        }

        if (collision)
            cout << "NO" << endl;
        else
            cout << "YES" << endl;
    }
}
