#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        string s;
        cin >> s;
        map<string, string> tails = {
            {"po", "FILIPINO"},
            {"desu", "JAPANESE"},
            {"masu", "JAPANESE"},
            {"mnida", "KOREAN"}
        };

        for (map<string, string>::iterator it = tails.begin(); it != tails.end(); it++) {
            string suffix = it->first;
            string country = it->second;

            bool done = true;
            for (int i = 0; i < suffix.length(); i++) {
                if (s[s.length() - 1 - i] != suffix[suffix.length() - 1 - i]) {
                    done = false;
                    break;
                }
            }
            if (done)
                cout << country << endl;
        }
    }
}
