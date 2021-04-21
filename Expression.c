#include<stdio.h>
int main(){
    int a,b,c,arr[8];
    scanf("%d %d %d", &a, &b, &c);
    arr[0] = a + b + c;
    arr[1] = (a + b) * c;
    arr[2] = a * (b + c);
    arr[3] = a * b * c;
    c = arr[0];
    for(int i = 1; i < 4; i++){
        if(arr[i] > c)
            c = arr[i];
    }
    printf("%d", c);
}
