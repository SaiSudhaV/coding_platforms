int Solution :: solve(vector<int> &A, int B) {
    unordered_map<int, int> tem;
    int res = 0, count = 0, n = (int)A.size();
    tem[0]++;
    for(int i = 0; i < n; i++) {
        count += A[i] % 2;
        res = res + tem[count - B];
        tem[count]++;
    }
    return res;
}