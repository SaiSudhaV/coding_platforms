#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int t, temp;
    long long int sum, n = 0;
    scanf("%d", &t);
    for(int i = 0; i < t; i++){
        sum = 0;
        scanf("%lld", &n);
        for(int j = 0; j < n; j++){
            scanf("%d", &temp);
            sum += (long long)temp;
        }
        printf("%lld\n", sum);
    }
    return 0;
}

