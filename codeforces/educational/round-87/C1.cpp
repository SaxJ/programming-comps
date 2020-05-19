#include <bits/stdc++.h>
using namespace std;

#define PI 3.14159265

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int n;
        cin >> n;

        long double angle = (((long double)360 / (2 * n)) / 2) * (PI / 180);
        long double toFlat = 0.5 / tan(angle);

        cout << (2 * toFlat) << endl;
    }
}
