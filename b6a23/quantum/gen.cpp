
#include <bits/stdc++.h>
using namespace std;

typedef unsigned long long int ulli;

int main() {
    mt19937_64 rng1, rng2;
    ulli seed = 1116; // same seed
    ulli n = 64;
    rng1.seed(seed);
    rng2.seed(seed);
    vector<int> probs = {1, 1};
    auto distrib = discrete_distribution(probs.begin(), probs.end());

    for (int i = 0; i < n; i++) {
        ulli res1 = distrib(rng1);
        printf("%llu", res1);
    }
    printf(" - from distribution\n");

    for (int i = 0; i < n; i++) {
        ulli res2 = rng2();
        printf("%llu", res2 >> 63);
    }
    printf(" - from msb\n");

    return 0;
}
