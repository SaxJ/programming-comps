#include <bits/stdc++.h>
#include <string.h>

using namespace std;

class Solution {
public:
  vector<size_t> allOccurrances(string needle, string haystack) {
    size_t pos = haystack.find(needle, 0);
    vector<size_t> positions;

    while (pos != string::npos) {
      positions.push_back(pos);
      pos = haystack.find(needle, pos + 1);
    }

    return positions;
  }

  bool checkString(string s) {
    vector<size_t> as = allOccurrances("a", s);
    vector<size_t> bs = allOccurrances("b", s);
  }
}
