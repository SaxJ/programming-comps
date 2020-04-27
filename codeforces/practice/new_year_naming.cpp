#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    string ns[n];
    string ms[m];
    for (int i = 0; i < n; i++)
        cin >> ns[i];
    for (int i = 0; i < m; i++)
        cin >> ms[i];

    int q;
    cin >> q;
    for (int i = 0; i < q; i++) {
        long long year;
        cin >> year;
        string x = ns[(year - 1) % n];
        string y = ms[(year - 1) % m];

        cout << (x + y) << endl;
    }
}
