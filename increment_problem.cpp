vector<int> Solution::solve(vector<int> &A) {
    unordered_map<int, set<int>> temp;
    vector<int> res;
    int n = A.size(), i = 0;
    for(; i < n; i++){
        if(temp.find(A[i]) != temp.end()){
            int idx = *(temp[A[i]].begin());
            res[idx]++;
            temp[A[i]].erase(temp[A[i]].begin());
            temp[res[idx]].insert(idx);
        }
        res.push_back(A[i]);
        temp[A[i]].insert(i);
    }
    return res;
}