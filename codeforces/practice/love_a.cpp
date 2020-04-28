#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    cin >> s;
    int as = 0;
    for (char& c : s) {
        if (c == 'a')
            as++;
    }
    int l = (as * 2) - 1;

    if (as > s.length() / 2)
        cout << s.length() << endl;
    else
        cout << l << endl;
}
