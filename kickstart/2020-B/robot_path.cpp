#include <bits/stdc++.h>
using namespace std;

long long bound(long long x) {
  if (x > 1000000000) {
    return 1000000000 - (x % 1000000000);
  } else if (x <= 0) {
    return 1000000000 + (x % 1000000000);
  } else {
    return x;
  }
}

int main() {
  long long T;
  cin >> T;
  for (long long t = 0; t < T; t++) {
    string program;
    cin >> program;

    stack<pair<long long, long long>> diffs;
    stack<long long> mults;
    diffs.push(pair<long long, long long>(1, 1));

    for (char &c : program) {
      if (c == '(')
        diffs.push(pair<long long, long long>(0, 0));
      else if (c == ')') {
        long long m = mults.top();
        mults.pop();

        pair<long long, long long> diff = diffs.top();
        long long dx = diff.first;
        long long dy = diff.second;
        diffs.pop();

        pair<long long, long long> top = diffs.top();
        diffs.pop();
        top.first = (top.first + dx * m) % 1000000000;
        top.second = (top.second + dy * m) % 1000000000;
        diffs.push(top);
      } else if (isdigit(c)) {
        mults.push((int)c - 48);
      } else {
        auto top = diffs.top();
        diffs.pop();

        switch (c) {
        case 'N':
          top.second = (top.second - 1);
          break;
        case 'S':
          top.second = (top.second + 1);
          break;
        case 'E':
          top.first = (top.first + 1);
          break;
        case 'W':
          top.first = (top.first - 1);
          break;
        }
        diffs.push(top);
      }
    }

    long long x = bound(diffs.top().first);
    long long y = bound(diffs.top().second);
    cout << "Case #" << t + 1 << ": " << x << " " << y << endl;
  }
}
