#include <bits/stdc++.h>
using namespace std;

int nums[200];

int main() {
  int T;
  cin >> T;
  for (int t = 0; t < T; t++) {
    int N;
    cin >> N;
    for (int n = 0; n < N; n++) {
      cin >> nums[n];
    }
    int peaks = 0;
    for (int i = 1; i < N - 1; i++) {
      if (nums[i - 1] < nums[i] && nums[i + 1] < nums[i])
        peaks++;
    }

    cout << "Case #" << t + 1 << ": " << peaks << endl;
  }
}
