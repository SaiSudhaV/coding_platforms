#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {  
    int mat1[100][100], sum, m, n, i, j;
    scanf("%d %d", &m, &n);
    for(i = 0; i < m; i++)
        for(j = 0; j < n; j++)
            scanf("%d", &mat1[i][j]);
    for(i = 0; i < m; i++){
        sum = 0;
        for(j = 0; j < n; j++)
            
            sum = sum + mat1[i][j];
        printf("%d\n", sum);
    }
    return 0;
}
