#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    string line;
    cin >> line;
    int ant = 0;
    int dan = 0;
    for (int i = 0; i < n; i++) {
        char c = line[i];
        if (c == 'A')
            ant++;
        else
            dan++;
    }
    if (ant > dan)
        cout << "Anton" << endl;
    else if (dan > ant)
        cout << "Danik" << endl;
    else
        cout << "Friendship" << endl;
}
