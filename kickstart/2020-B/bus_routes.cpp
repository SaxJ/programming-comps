#include <bits/stdc++.h>
using namespace std;

long long nums[2000];

bool travel(long start, long long arr[], long long N, long long limit) {
  long days = start;
  for (int i = 1; i < N; i++) {
    long n = arr[i];
    long f = ceil((float)days / n);
    days = f * n;
    if (days > limit)
      return false;
  }
  return true;
}

int search(long end, long long arr[], long long D) {
  long max = 0;
  int idx = -1;
  for (int i = 0; i <= end; i++) {
    if (arr[i] > max) {
      max = arr[i];
      idx = i;
    }
  }

  return idx;
}

int main() {
  long long T;
  cin >> T;
  for (int t = 0; t < T; t++) {
    long long N, D;
    cin >> N >> D;
    for (int n = 0; n < N; n++) {
      cin >> nums[n];
    }
    int end = N - 1;
    long long limit = D;
    while (end > 1) {
      int maxIndex = search(end, nums, limit);
      int maxFactor = limit / nums[maxIndex];

      limit = nums[maxIndex] * maxFactor;
      end = maxIndex - 1;
    }

    long ans = (limit / nums[0]) * nums[0];
    cout << "Case #" << t + 1 << ": " << ans << endl;
  }
}
