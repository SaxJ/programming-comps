#include <bits/stdc++.h>
using namespace std;

class Solution {
private:
  map<int, bool> cache;
  map<int, bool>::iterator it;

public:
  Solution() {
    cache.insert(pair<int, bool>(1, false));
    cache.insert(pair<int, bool>(2, true));
  }

  bool divisorGame(int N) {
    if (cache.find(N) != cache.end())
      return cache.find(N)->second;
    else {
      return !divisorGame(N - 1);
    }
  }
};

int main() {
  Solution sln;
  cout << (sln.divisorGame(10) ? "true" : "false") << endl;
}
