#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int n, k;
        cin >> n >> k;
        int mounts[n];
        for (int i = 0; i < n; i++)
            cin >> mounts[i];

        int maxPeaks = 0;
        int start = 0;
        queue<int> peaks;

        for (int i = 1; i < k - 1; i++) {
            int idx = start + i;
            int c = mounts[idx];
            if (mounts[idx - 1] < c && c > mounts[idx + 1]) {
                maxPeaks++;
                peaks.push(idx);
            }
        }
        cout << "inspecting " << 0 << ", " << (k - 1) << endl;

        for (int s = 1; s <= n-k; s++) {
            int backPeak = peaks.front();
            if (s == backPeak) {
                peaks.pop();
            }

            int end = s + k - 2;
            int x = end + 1;
            cout << "inspecting " << s << ", " <<  x << endl;
            if (mounts[end-1] < mounts[end] && mounts[end] > mounts[end+1]) {
                peaks.push(end);
            }
            if (peaks.size() > maxPeaks) {
                start = s;
                maxPeaks = peaks.size();
            }
        }

        int mp = maxPeaks + 1;
        int idx = start + 1;
        cout << mp << " " << idx << endl;
    }
}
