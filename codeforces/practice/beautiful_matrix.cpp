#include <bits/stdc++.h>
using namespace std;

int main() {
    int x, y;
    for (int i = 1; i <= 5; i++) {
        for (int j = 1; j <= 5; j++) {
            int n;
            cin >> n;
            if (n == 1) {
                x = i;
                y = j;
            }
        }
    }
    cout << (abs(x - 3) + abs(y - 3)) << endl;
}
