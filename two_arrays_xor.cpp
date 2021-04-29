int Solution::solve(vector<int> &A, vector<int> &B) {
    int tem = 0, max_xor = 0, i = 31, m = A.size(), n = B.size();
    unordered_set<int> tem1, tem2;
    for(; i >= 0; i--) {
        tem1 = {};
        tem2 = {};
        tem |= 1 << i;
        int k = max_xor | (1 << i);
        for(int j = 0; j < m; j++)
            tem1.insert(A[j] & tem);
        for(int j = 0; j < n; j++)
            tem2.insert(B[j] & tem);
        for(int j : tem1)
            if(tem2.count(j ^ k)) {
                max_xor = k;
                break;
            }
    }
    return max_xor;
}