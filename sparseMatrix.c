#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int mat1[100][100], total, count = 0, m, n, i, j;
    scanf("%d %d", &m, &n);
    for(i = 0; i < m; i++){
        for(j = 0; j < n; j++)
            scanf("%d", &mat1[i][j]);
    }
    for(i = 0; i < m; i++)
        for(j = 0; j < n; j++)
            if(mat1[i][j] == 0)
                count++;
    total = n * m;
    if(count > total / 2)
        printf("Yes");
    else
        printf("No");
    return 0;
}
