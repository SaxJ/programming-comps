#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;

    int r = n % 10;
    if (r == 2 || r == 4 || r == 5 || r == 7 || r == 9)
        cout << "hon" << endl;
    else if (r == 0 || r == 1 || r == 6 || r == 8)
        cout << "pon" << endl;
    else
        cout << "bon" << endl;
}
