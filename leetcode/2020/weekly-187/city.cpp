#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string destCity(vector<vector<string>>& paths) {
        set<string> all;
        set<string> outgoing;
        for (int i = 0; i < paths.size(); i++) {
            vector<string> path = paths[i];
            all.insert(path[0]);
            all.insert(path[1]);
            outgoing.insert(path[0]);
        }

        vector<string> result(2 * paths.size());
        set_difference(all.begin(), all.end(), outgoing.begin(), outgoing.end(), result.begin());
        return *result.begin();
    }
};
