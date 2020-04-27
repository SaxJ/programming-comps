#include <bits/stdc++.h>
using namespace std;

bool comp(pair<int, int> a, pair<int, int> b) { return (a.second > b.second); }

int main() {
  int N;
  cin >> N;
  vector<pair<int, int>> orig;
  for (int i = 0; i < N; i++) {
    int x;
    cin >> x;
    pair<int, int> p(i, x);
    orig.push_back(p);
  }
  sort(orig.begin(), orig.end(), comp);

  int start = 0;
  int end = N;
  long long total = 0;
  for (int i = 0; i < N; i++) {
    pair<int, int> current = orig[i];
    int op = current.first;
    int distStart = abs(op - start);
    int distEnd = abs(op - end);
    if (distStart > distEnd) {
      total += current.second * distStart;
      start++;
    } else {
      total += current.second * distEnd;
      end--;
    }
  }

  cout << total << endl;
}
