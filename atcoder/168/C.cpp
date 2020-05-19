#include <bits/stdc++.h>
using namespace std;

int main() {
    int a, b;
    double h, m;
    cin >> a >> b >> h >> m;

    double a1 = (2 * M_PI) * (h / 12) + (2 * M_PI) * (m / (60 * 12));
    double a2 = (2 * M_PI) * (m / 60);
    double diff = max(a1, a2) - min(a1, a2);

    cout << "angle = " << (diff / (2 * M_PI) * 360) << endl;

    if (diff > M_PI)
        diff = (2 * M_PI) - diff;


    double ds = a * a + b * b - 2 * a * b * cos(diff);
    cout << sqrt(ds) << endl;
}

/**
a, b, h, m = [int(x) for x in input().split(' ')]

a1 = (2 * math.pi) * (h / 12)
a2 = (2 * math.pi) * (m / 60)
diff = max(a1, a2) - min(a1, a2)
if diff > math.pi:
    diff = (2 * math.pi) - diff

ds = a * a + b * b - 2 * a * b * math.cos(diff)
print(math.sqrt(ds))
**/
