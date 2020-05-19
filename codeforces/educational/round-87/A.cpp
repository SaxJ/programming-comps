#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    cin >> T;

    for (int t = 0; t < T; t++) {
        long atLeast, firstAlarm, alarm, toSleep;
        cin >> atLeast >> firstAlarm >> alarm >> toSleep;

        if (firstAlarm >= atLeast) {
            cout << firstAlarm << endl;
            continue;
        }
        if (toSleep >= alarm) {
            cout << "-1" << endl;
            continue;
        }
        long remaining = atLeast - firstAlarm;
        long sleepEach = alarm - toSleep;
        long units = remaining / sleepEach;
        if (remaining % sleepEach == 0) {
            cout << (firstAlarm + units * alarm) << endl;
        } else {
            cout << (firstAlarm + (units + 1) * alarm) << endl;
        }
    }
}
