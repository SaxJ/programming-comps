#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;

    string commands;
    cin >> commands;

    int lefts = 0;
    int rights = 0;
    for (int i = 0; i < n; i++) {
        char c = commands[i];
        if (c == 'L')
            lefts++;
        else
            rights++;
    }
    cout << (lefts + rights + 1) << endl;
}
