#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int n, k;
        cin >> n >> k;

        string resultEven = "";
        string resultOdd = "";
        int totalEven = 0;
        int totalOdd = 0;
        for (int i = 0; i < k - 1; i++) {
            resultEven += to_string(2) + " ";
            resultOdd += to_string(1) + " ";
            totalEven += 2;
            totalOdd++;
        }

        int remainderEven = n - totalEven;
        int remainderOdd = n - totalOdd;

        if (remainderEven % 2 == 0 && remainderEven > 0) {
            cout << "YES" << endl;
            cout << resultEven << remainderEven << endl;
        } else if (remainderOdd % 2 != 0 && remainderOdd > 0) {
            cout << "YES" << endl;
            cout << resultOdd << remainderOdd << endl;
        } else {
            cout << "NO" << endl;
        }
    }
}

