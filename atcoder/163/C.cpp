#include <bits/stdc++.h>
using namespace std;

int main() {
  int N;
  cin >> N;

  int seen[N];
  fill(seen, seen + N, 0);

  for (int i = 1; i < N; i++) {
    int a;
    cin >> a;
    seen[a - 1]++;
  }
  for (int i = 0; i < N; i++) {
    cout << seen[i] << endl;
  }
}
