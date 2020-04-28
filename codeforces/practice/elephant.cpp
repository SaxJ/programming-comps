#include <bits/stdc++.h>
using namespace std;

int main() {
    int x;
    cin >> x;

    int steps = 0;
    steps += x / 5;
    x %= 5;

    steps += x / 4;
    x %= 4;

    steps += x / 3;
    x %= 3;

    steps += x / 2;
    x %= 2;

    steps += x;
    cout << steps << endl;
}
