int Solution::solve(int A, vector<vector<int> > &B) {
    map<int, int> edge, root;
    int res = INT_MIN, count = 0;
    for(int i = 0; i < B.size(); i++){
        int node = B[i][0], temp = B[i][1];
        edge[node]++;
        root[temp] = node;
        res = max({res, node, temp});
    }
    for(int i = res; i > 1; i--){
        if(edge[i] % 2 != 0){
            count++;
            edge[root[i]]--;
        }
    }
    return count;
}