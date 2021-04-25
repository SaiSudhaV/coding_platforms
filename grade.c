#include <stdio.h>

int main(void) {
    int n, h, c, t;
    int i, j, k;
    scanf("%d", &n);
    for(int l = 0; l < n; l++){
        scanf("%d %d %d", &h, &c, &t);
        i = h > 50;
        j = c < 0.7;
        k = t > 5600;
        if(i && j && k)
            printf("10\n");
        else if(i && j)
            printf("9\n");
        else if(j && k)
            printf("8\n");
        else if(i && k)
            printf("7\n");
        else if(i || j || k)
            printf("6\n");
        else
            printf("5\n");
    }
	return 0;
}

