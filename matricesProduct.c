#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
   
int main()  
{  
    int t, n1, m1, n2, m2, mat1[100][100], mat2[100][100], product[100][100];
    scanf("%d", &t);
    for(int i = 0; i < t; i++){
        scanf("%d %d", &n1, &m1);
        for(int j = 0; j < n1; j++)
            for(int k = 0; k < m1; k++)
                scanf("%d", &mat1[j][k]);
        scanf("%d %d", &n2, &m2);
        for(int j = 0; j < n2; j++)
            for(int k = 0; k < m2; k++)
                scanf("%d", &mat2[j][k]);
        if (m1 != n2) 
            return 0;  
        for(int l = 0; l < n1; l++) 
            for(int j = 0; j < m2; j++){
                product[l][j] = 0;
                for(int k = 0; k < n2; k++)
                    product[l][j] += mat1[l][k] * mat2[k][j];
            }
        for(int k = 0; k < n1; k++){
            for(int j = 0; j < m2; j++)
                printf("%d ", product[k][j]);
            printf("\n");
        }
    }
    return 0;  
}
