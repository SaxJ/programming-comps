#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findComplement(int num) {
        bitset<32> bits = bitset<32>(num);
        int firstOn = 0;
        for (int i = 0; i < 32; i++) {
            if (bits[i] == 1) {
                firstOn = i;
                break;
            }
        }

        for (int i = firstOn; i < 32; i++)
            bits[i] = !bits[i];


        unsigned long result = bits.to_ulong();
        return result;
    }
};
