#include <stdio.h>

int main(void) {
    char ch;
    scanf("%c", &ch);
    if(65 <= ch && ch <= 90){
        if(ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U')
            printf("Vowel");
        else
            printf("Consonant");
    }
	return 0;
}