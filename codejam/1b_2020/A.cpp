#include <bits/stdc++.h>
using namespace std;

map<string, pair<int, int>> moves = {
    {"N", {0, 1}}, {"N", {0, -1}}, {"N", {1, 0}}, {"N", {-1, 01}}};

int main() {
  int T;
  cin >> T;
  for (int t = 0; t < T; t++) {
    long X, Y;
    cin >> X >> Y;

    queue<tuple<int, int, int, string>> qu;
    qu.push(tuple<int, int, int, string>(1, -1, 0, "W"));
    qu.push(tuple<int, int, int, string>(1, 1, 0, "E"));
    qu.push(tuple<int, int, int, string>(1, 0, 1, "N"));
    qu.push(tuple<int, int, int, string>(1, 0, -1, "S"));

    bool found = false;
    while (qu.size()) {
      tuple<int, int, int, string> current = qu.front();
      int x = get<1>(current);
      int y = get<2>(current);
      string p = get<3>(current);
      int nStep = 2 * get<0>(current);
      qu.pop();
      if (x == X && y == Y) {
        cout << "Case #" << t + 1 << ": " << p << endl;
        found = true;
        break;
      } else if (abs(x) > abs(X) || abs(y) > abs(Y)) {
        continue;
      } else {
        int dx = 1;
        int dy = 0;
        int xx = x + dx * nStep;
        int yy = y + dy * nStep;
        if (abs(xx) <= 1000000000 and abs(yy) <= 1000000000) {
          qu.push(tuple<int, int, int, string>(nStep, xx, yy, p + "E"));
        }

        dx = -1;
        dy = 0;
        xx = x + dx * nStep;
        yy = y + dy * nStep;
        if (abs(xx) <= 1000000000 and abs(yy) <= 1000000000) {
          qu.push(tuple<int, int, int, string>(nStep, xx, yy, p + "W"));
        }

        dx = 0;
        dy = -1;
        xx = x + dx * nStep;
        yy = y + dy * nStep;
        if (abs(xx) <= 1000000000 and abs(yy) <= 1000000000) {
          qu.push(tuple<int, int, int, string>(nStep, xx, yy, p + "S"));
        }

        dx = 0;
        dy = 1;
        xx = x + dx * nStep;
        yy = y + dy * nStep;
        if (abs(xx) <= 1000000000 and abs(yy) <= 1000000000) {
          qu.push(tuple<int, int, int, string>(nStep, xx, yy, p + "N"));
        }
      }
    }
    if (!found) {
      cout << "Case #" << t + 1 << ": IMPOSSIBLE" << endl;
    }
  }
}
