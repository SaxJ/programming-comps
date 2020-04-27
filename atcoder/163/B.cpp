#include <bits/stdc++.h>
using namespace std;

int main() {
  int N, M;
  cin >> N >> M;
  long total = 0;
  for (int i = 0; i < M; i++) {
    int x;
    cin >> x;
    total += x;
  }

  if (total > N) {
    cout << "-1" << endl;
  } else {
    cout << N - total << endl;
  }
}
