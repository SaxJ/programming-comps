#include <bits/stdc++.h>

using namespace std;

vector<size_t> allOccurrances(string needle, string haystack) {
    size_t pos = haystack.find(needle, 0);
    vector<size_t> positions;

    while(pos != string::npos)
    {
        positions.push_back(pos);
        pos = haystack.find(needle, pos+1);
    }

    return positions;
}

int main(int argc, char *argv[]) {
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        int n;
        cin >> n;
        string input;
        cin >> input;

        vector<size_t> chefs = allOccurrances("chef", input);
        vector<size_t> codes = allOccurrances("code", input);

        bool success = true;
        int b = 0;

        for (int a = 0; a < chefs.size(); a++) {
            while (b < codes.size()) {
                if (codes[b] <= chefs[a]) {
                    break;
                }

                b++;
            }

            if (b >= codes.size()) {
                success = false;
                break;
            }

        }

        if (success)
            cout << "AC" << endl;
        else
            cout << "WA" << endl;
    }
    return 0;
}
