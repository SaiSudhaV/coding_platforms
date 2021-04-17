#include <iostream>

int main() {
    int t, i;
    long long int n, m, k, n, d, ft, num;
    cin >> t;
    for(i = 0; i < T; i++) {
        cin >> n, m, k;
        scanf("%lld %lld %lld", &a, &l, &s);
        tem = (long long int)(2 * k)/(n + l);
        tem1 = (long long int)(m - a)/(tem - 5);
        res = (long long int)(((2 * k) / tem) - (tem - 1) * tem1) / 2;

        if (i >= 1)
            cout << "\n" <<(long long int)tem << endl;
        else
            cout << (long long int)tem << endl;
        while(n >= 1) {
            cout << (long long int)tem << endl;
            ft += d;
            n--;
        }
    }
}