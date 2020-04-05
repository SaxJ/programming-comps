#include <iostream>
using namespace std;

int main() {
  int n;
  cin >> n;
  bool fail = false;
  for (int i = 0; i < n; i++) {
    int p;
    cin >> p;
    if (p == 1) {
      fail = true;
      break;
    }
  }
  if (fail) {
    cout << "HARD";
  } else {
    cout << "EASY";
  }
}
