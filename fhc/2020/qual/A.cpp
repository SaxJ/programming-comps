#include <bits/stdc++.h>

using namespace std;

char solve(int N, string ins, string outs, int from, int to) {
    if (from == to)
        return 'Y';
    int d = (from < to) ? -1 : 1;

    for (int i = from  + d; i != to; i += d) {
        if (outs[i-1] == 'N' || ins[i] == 'N')
            return 'N';
    }

    return (outs[to - 1] == 'N' || ins[to] == 'N') ? 'N' : 'Y';
}

int main() {
    int T;
    cin >> T;

    for (int t = 0; t < T; t++) {
        int N;
        cin >> N;
        string ins, outs;
        cin >> ins >> outs;

        cout << "Case #" << (t + 1) << ":" << endl;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                cout << solve(N, ins, outs, i, j);
            }
            cout << endl;
        }
    }
}
