#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    string days;
    cin >> days;
    char last = days[0];
    int sf = 0;
    int fs = 0;
    for (int i = 1; i < n; i++) {
        char c = days[i];
        if (last != c) {
            if (c == 'S') fs++;
            if (c == 'F') sf++;
        }
        last = c;
    }
    if (sf > fs)
        cout << "YES" << endl;
    else
        cout << "NO" << endl;
}
