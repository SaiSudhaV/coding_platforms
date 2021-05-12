#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int i, j, k;
    char str[100];
    scanf("%d", &k);
    
    for(j = 0; j < k; j++){
        scanf("%s", str);
      for(i = 0; str[i] != '\0' ; i++){
        if(i == 0 || i % 2 == 0)
            printf("%c", str[i]);
    }
    printf(" ");
    for (i = 1; str[i] != '\0'; i++) {
      if (i % 2 != 0)
        printf("%c", str[i]);
    } 
    printf("\n"); 
    }
    

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    return 0;
}
