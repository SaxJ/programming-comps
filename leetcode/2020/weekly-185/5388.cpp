#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  string reformat(string s) {
    vector<char> alphas;
    vector<char> nums;
    for (char &c : s) {
      if (isdigit(c))
        nums.push_back(c);
      if (isalpha(c))
        alphas.push_back(c);
    }

    int a = alphas.size();
    int n = nums.size();
    if (!(a == n - 1 || n == a - 1 || n == a))
      return "";

    vector<char> longer = (alphas.size() > nums.size()) ? alphas : nums;
    vector<char> shorter = (alphas.size() <= nums.size()) ? alphas : nums;
    string output = "";
    for (int i = 0; i < s.length(); i++) {
      if (i % 2 == 0) {
        output += longer.back();
        longer.pop_back();
      } else {
        output += shorter.back();
        shorter.pop_back();
      }
    }
    return output;
  }
};
