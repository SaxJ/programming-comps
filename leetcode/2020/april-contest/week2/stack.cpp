#include <bits/stdc++.h>
using namespace std;

class MinStack {
private:
  stack<int> mainStack;
  stack<int> minStack;
  int currentMin;

public:
  /** initialize your data structure here. */
  MinStack() { currentMin = numeric_limits<int>::max(); }

  void push(int x) {
    if (x < currentMin) {
      currentMin = x;
    }

    mainStack.push(currentMin);
    mainStack.push(x);
  }

  void pop() {
    if (!mainStack.empty()) {
      mainStack.pop();
      minStack.pop();
    }
    currentMin = minStack.empty() ? numeric_limits<int>::max() : minStack.top();
  }

  int top() { return mainStack.top(); }

  int getMin() { return minStack.top(); }
};

int main() {
  MinStack stk;
  stk.push(-2);
  stk.push(0);
  stk.push(-3);
  cout << stk.getMin();
  stk.pop();
  cout << stk.getMin();
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(x);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
