//your code goes here
#include <stdio.h>

using namespace std;

int main() {
    long long t, n, rem, tem;
	char s[255];
    scanf("%lld", &t);
    for(int i = 0; i < t; i++) {
		scanf("%lld %s",&n, s);
		if(n != 0){
            rem = 0;
            tem = 0;
			while(s[j] != '\0'){
                tem++;
                rem *= 10;
                rem = (rem + s[j] - 48) % n;
			}
			printf("%lld\n", __gcd(n, rem));
        } else
			printf("%s\n",s);
  }
	return 0;
}