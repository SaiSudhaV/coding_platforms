#include <iostream>

using namespace std;

int main() {
    int t, i;
    long long int s, a, l, d, ft, n, num;
    cin >> t;
    for(i = 0; i < t; i++) {
        cin >> a >> l >> s;
        n = (long long int)(2 * s)/(a + l);
        d = (long long int)(l - a)/(n - 5);
        ft = (long long int)(((2*s)/n)-(n-1)*d)/2;
        num = (long long int)n;

        if (i >= 1)
            printf("\n%lld\n", num);
        else
            printf("%lld\n", num);
        while(n >= 1) {
            printf("%lld ", ft);
            ft += d;
            n--;
        }
    }
}