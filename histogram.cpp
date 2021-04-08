#include <iostream>
#include <bits/stdc++.h>

using namespace std;

long long maxArea(ar, n){
    long long count = 1, low = arr[0], high = arr[0];
    for (int i = 1; i < n; i++) {
        low = min(low, arr[i]);
        count++;
        if(arr[i] > count*low) {
            low = arr[i];
            count = 1;
            high = max(high,arr[i]);
        }else
            high = max(high,count * low);
    }
    return high;
}

int main () {
    while(true){
        int n;
        cin >> n;
        if(n == 0)
            break;
        long long ar[n], count = 1;
        for (int i = 0; i < n; i++)
            cin >> ar[i];
        cout << maxArea(ar, n) << endl;
    }
}