#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int n;
        cin >> n;
        string sn = to_string(n);
        vector<int> addends;
        int fac = 1;
        for (int i = sn.length() - 1; i >= 0; i--) {
            char cc = sn[i];
            int c = cc - 48;
            if (c != 0)
                addends.push_back(fac * c);
            fac *= 10;
        }
        cout << addends.size() << endl;
        for (int i = 0; i < addends.size(); i++) {
            cout << addends[i];
            if (i != addends.size() - 1)
                cout << " ";
        }
        cout << endl;
    }
}
