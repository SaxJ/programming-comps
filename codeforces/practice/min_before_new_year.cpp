#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int h, m;
        cin >> h >> m;
        int hours = 23 - h;
        int mins = 60 - m;
        cout << (60 * hours + mins) << endl;
    }
}
