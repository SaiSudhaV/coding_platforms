#include <stdio.h>

int min_moves(int h, int h1, int w, int w1) {
    int res = 0;
    while(h > h1){
        if((h / 2) < (h - h1))
            h = h / 2;
        else 
            h = h1;
        ++res;
    }
    while(w > w1){
        if((w / 2) < (w - w1))
            w = w / 2;
        else 
            w = w1;
        ++res;
    }
    return res;
}

int main() {
    int h, w, h1, w1;
    scanf("%d %d %d %d", &h, &w, &h1, &w1);
    if(!((h < h1) || (w < w1)))
        printf("%d", min_moves(h, h1, w, w1));
    return 0;
}