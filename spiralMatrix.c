#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {  
    int t, m, mat1[100][100];
    scanf("%d", &t);
    for(int i = 0; i < t; i++){
        scanf("%d", &m);
        for(int j = 0; j < m; j++)
            for(int k = 0; k < m; k++)
                scanf("%d", &mat1[j][k]);
        int x, a = 0, b = 0, n = m;
        while (a < m && b < n) {
            for (x = b; x < n; x++) 
                printf("%d ", mat1[a][x]); 
            a += 1; 
            for (x = a; x < m; x++) 
                printf("%d ", mat1[x][n - 1]); 
            n -= 1; 
            if (a < m){
                for (x = n - 1; x >= b; x--)
                    printf("%d ", mat1[m - 1][x]); 
                m -= 1;
            }
            if (b < n){
                for (x = m - 1; x >= a; x--) 
                    printf("%d ", mat1[x][b]); 
                b += 1; 
            }
        }
        printf("\n");
    }
    return 0;  
}
