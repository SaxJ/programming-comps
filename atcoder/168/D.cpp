#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    map<int, set<int>> adj;
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;

        if (adj.find(a) == adj.end())
            adj[a] = set<int>();
        if (adj.find(b) == adj.end())
            adj[b] = set<int>();

        adj[a].insert(b);
        adj[b].insert(a);
    }

    stack<int> stk;
    stk.push(1);
    set<int> seen;
    map<int, int> parent;
    while (!stk.empty()) {
        int current = stk.top();
        stk.pop();

        seen.insert(current);

        set<int> ns = adj.at(current);
        for (auto i : ns) {
            if (seen.find(i) == seen.end()) {
                seen.insert(i);
                stk.push(i);
                parent[i] = current;
            }
        }
    }

    if (seen.size() == n) {
        cout << "Yes" << endl;
        for (int i = 2; i <= n; i++)
            cout << parent[i] << endl;
    } else
        cout << "No" << endl;
}

