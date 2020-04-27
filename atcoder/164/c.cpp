#include <bits/stdc++.h>
using namespace std;

int main() {
    long n;
    cin >> n;
    set<string> items;
    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        items.insert(s);
    }
    cout << items.size() << endl;
}
