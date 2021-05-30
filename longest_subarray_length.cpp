int Solution::solve(vector<int> &A) {
    int n = A.size();
    for(int i = 0; i < n; i++)
        if(A[i] == 0)
            A[i] = -1;
    int tot = 1, ptr = 0, p = 0, res = 0;
    unordered_map<int, int> tem;
    for(int i = 0; i < n; i++) {
        ptr += A[i];
        if(ptr == tot){
            p = i + 1;
            if(p > res)
                res = p;
        }
        if (tem.find(ptr) == tem.end())
            tem[ptr] = i;
        if(tem.find(ptr - tot) != tem.end()) {
            p = i - tem[ptr - tot];
            if(p > res)
                res = p;
        }
    }
    return res;
}
