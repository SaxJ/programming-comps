#include <bits/stdc++.h>
using namespace std;

int main() {
    unsigned long long int x, total;
    total = 100;
    cin >> x;

    int year = 0;
    while (total < x) {
        total += 1.01 * total;
        year++;
    }
    cout << year;
}
