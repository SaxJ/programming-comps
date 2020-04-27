#include <bits/stdc++.h>
using namespace std;

int main() {
    long a, b, c, d;
    cin >> a >> b >> c >> d;
    int turn = 0;
    while (a > 0 && c > 0) {
        if (turn % 2 == 0) {
            c -= b;
            if (c <= 0)
                cout << "Yes" << endl;
        } else {
            a -= d;
            if (a <= 0)
                cout << "No" << endl;
        }
        turn++;
    }
}
