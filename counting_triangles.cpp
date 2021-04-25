int Solution::nTriang(vector<int> &A) {
    sort(A.begin(),A.end());
    int n = A.size(), res = 0, j, k;
    for(int i = n - 1;i>1;i--) {
        j = 0;
        k = i - 1;
        if(A[i] == 0)
            continue;
        while(j < k) {
            if(A[j] + A[k] > A[i]) {
                res += k - j;
                k--;
            } else
                j++;
            res %= 1000000007;
        }
    }
    return res;
}
