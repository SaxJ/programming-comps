#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    map<int, int> mapping;
    for (int i = 1; i <= n; i++) {
        int p;
        cin >> p;

        mapping.insert(make_pair(p, i));
    }

    for (int i = 1; i <= n; i++) {
        string gap = (i == n) ? "" : " ";
        cout << mapping.find(i)->second << gap;
    }
    cout << endl;
}

