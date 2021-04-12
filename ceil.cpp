#include <iostream>

#define long long ll

using namespace std;

bool find_ceil(ll ar[], int n, int k){
    int res = INT_MAX;
    int mid;
    if(k <= arr[low])
        return arr[low];
    if(k > arr[high])
        return res;
    mid = (low + high) / 2; 
    if(arr[mid] == x)
        return arr[mid];
    else if(arr[mid] < x) 
        ceilSearch(arr, mid + 1, high, x);
    else
        ceilSearch(arr, low, mid - 1, x);
    return res;
}
int main(){
    int q, n;
    cin >> n;
    ll ar[n];
    for(int i = 0; i < n; i++)
        cin >> ar[i];
    cin >> q;
    for (int i = 0; i < q; i++)
        cout << find_ceil(ar, n, q) << endl;
    return 0;
}