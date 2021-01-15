#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
  bool canFormArray(vector<int> &arr, vector<vector<int>> &pieces) {
    int position = 0;
    while (position < arr.size()) {
      int x = arr[position];

      vector<int> matching;
      for (vector<int> piece : pieces) {
        if (piece[0] == x) {
          matching = piece;
          break;
        }
      }

      if (matching.empty())
        return false;

      for (int m : matching) {
        if (m != arr[position])
          return false;
        position++;
      }
    }
    return true;
  }
};
