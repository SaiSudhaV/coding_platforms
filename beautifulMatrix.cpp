#include <iostream>
using namespace std;
 
int main() {
    int mat[6][6], m = 0, n = 0;
    for(int i = 0; i < 5; i++)
        for(int j = 0; j < 5; j++)
            cin >> mat[i][j] ;
    for(int i = 0; i < 5; i++)
        for(int j = 0; j < 5; j++)
            if(mat[i][j] == 1){
                m = i + 1;
                n = j + 1;
            }
    cout << abs(m - 3) + abs(n - 3);
    return 0;
}
