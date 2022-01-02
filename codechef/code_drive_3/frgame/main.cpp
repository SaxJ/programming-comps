#include <iostream>

using namespace std;

int main() {
    long t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        long a, b, c, d;
        cin >> a >> b >> c >> d;

        if (a < b) {
            a += c;
        } else {
            b += c;
        }

        if (a < b) {
            a += d;
        } else {
            b += d;
        }

        if (a >= b) {
            cout << 'N' << endl;
        } else {
            cout << 'S' << endl;
        }
    }
    return 0;
}
