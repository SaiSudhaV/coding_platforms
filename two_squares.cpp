#include <iostream>
#include <cmath>

using namespace std;

int T;
long long N;
int check_two_square(long long int n){
    int valid = 0;
    for(int i = 1; 1LL * i * i <= n; i ++){
        long long tem = n - 1LL * i * i;
        long long sq = (long long)sqrt(1. * tem);
        if(sq * sq == tem){
            valid = 1;
            break;
        }
    }
    return valid;
}
int main(void) {
    long long int t, n;
    cin >> t;
    while(t--){
        cin >> n;
        if(check_two_square(n))
            cout << "Yes" << endl;
        else
            cout << "No" << endl;
    }
    
    return 0;
}