#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    cin >> T;

    for (int t = 0; t < T; t++) {
        string s;
        cin >> s;
        map<char, int> seen;

        int l, r;
        l = r = 0;
        int size = 2000000;
        bool found = false;

        while (r < s.length()) {
            if (seen.find(s[r]) == seen.end())
                seen[s[r]] = 0;
            seen[s[r]]++;

            while (seen.size() == 3) {
                found = true;
                size = min(size, r - l + 1);
                seen[s[l]]--;
                if (seen[s[l]] == 0)
                    seen.erase(s[l]);
                l++;
            }
            r++;
        }

        if (found)
            cout << size << endl;
        else
            cout << 0 << endl;
    }
}
