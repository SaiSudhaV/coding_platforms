#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
long long int HCF(long long int n1, long long int n2) {
    if (n2 == 0)
        return n1;
    else
        return HCF(n2, n1 % n2);
}

long long int LCM(long long int n1, long long int n2) {
    return (n1 * n2) / HCF(n1, n2);
}

int main() {
    int t;
    long long int n1, n2;
    scanf("%d", &t);
    for(int i = 0; i < t; i++){
        scanf("%lld %lld", &n1, &n2);
        printf("%lld %lld\n", LCM(n1, n2), HCF(n1, n2));
    }
    return 0;
}
