#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;

    string last = "";
    int groups = 0;
    for (int i = 0; i < n; i++) {
        string magnet;
        cin >> magnet;

        if (last == "" || last == magnet)
            groups += 0;
        else
            groups++;
        last = magnet;
    }
    cout << (groups + 1) << endl;
}
