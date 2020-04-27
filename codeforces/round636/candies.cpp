#include <bits/stdc++.h>
using namespace std;
set<long> factors(long long n) {
    set<long> result;
    for (int i = 1; i < (pow(n, 0.5) + 1); i++) {
        long div = n / i;
        long mod = n % i;
        if (mod == 0) {
            result.insert(i);
            result.insert(div);
        }
    }
    return result;
}

bool closeEnough(double x) {
    long rounded = (long)x;
    double diff = fabs(rounded - x);
    return diff < 0.0001;
}

int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        long long n;
        cin >> n;
        set<long> fs = factors(n);
        long power = 1;
        long x;
        while (true) {
            double fx = -n / (1 - pow(2, power));
            if (closeEnough(fx)) {
                x = (long)fx;
                break;
            }
        }
        /*
        for (auto i = fs.begin(); i != fs.end(); i++) {
            long factor = *i;
            if (factor % 2 == 0)
                continue;
            else {
                double power = log2(n + 1);
                if (closeEnough(power)) {
                    x = -n / (1 - pow(2, (long)power));
                    break;
                }
            }
        }
        */
        cout << x << endl;
    }
}
