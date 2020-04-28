#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    set<int> switched;

    for (int i = 0; i < n; i++) {
        int connected;
        cin >> connected;

        for (int j = 0; j < connected; j++) {
            int idx;
            cin >> idx;
            switched.insert(idx);
        }
    }

    if (switched.size() == m)
        cout << "YES" << endl;
    else
        cout << "NO" << endl;
}

