void genCombination(vector<int>&, vector<vector<int>>& , vector<int>, int, int);

vector<vector<int> > Solution::combinationSum(vector<int> &A, int B) {
    vector<vector<int>> res;
    sort(A.begin(), A.end());
    int i = unique(A.begin(), A.end()) - A.begin();
    A.resize(i);
    genCombination(A, res, vector<int>(), 0, B);
    sort(res.begin(), res.end());
    return res;
}

void genCombination(vector<int>& A, vector<vector<int>>& res, vector<int> tem, int i, int B) {
    if (B == 0) { 
        res.push_back(tem); 
        return; 
    }
    if (i == A.size()) 
        return;
    int k = A[i++];
    do {
        genCombination(A, res, tem, i, B);
        B -= k, tem.push_back(k);
    } while(B >= 0);
}