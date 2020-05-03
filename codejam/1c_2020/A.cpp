#include <bits/stdc++.h>
using namespace std;

int distance(int x, int y) {
    return abs(x) + abs(y);
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int x, y;
        cin >> x >> y;

        string moves;
        cin >> moves;

        int chosen = -1;
        for (int i = 0; i < moves.length(); i++) {
            char c = moves[i];
            switch (c) {
                case 'N':
                    y++;
                    break;
                case 'S':
                    y--;
                    break;
                case 'E':
                    x++;
                    break;
                case 'W':
                    x--;
                    break;
            }

            int dist = distance(x, y);
            int time = i + 1;
            if (dist <= time) {
                chosen = time;
                break;
            }
        }

        if (chosen < 0)
            cout << "Case #" << t << ": " << "IMPOSSIBLE" << endl;
        else
            cout << "Case #" << t << ": " << chosen << endl;
    }
}
