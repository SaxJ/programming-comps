#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        long nStudents, maxScore;
        cin >> nStudents >> maxScore;
        long me;
        cin >> me;

        long total;
        for (int i = 1; i < nStudents; i++) {
            int score;
            cin >> score;
            total += score;
        }

        cout << min(total, maxScore) << endl;
    }
}


