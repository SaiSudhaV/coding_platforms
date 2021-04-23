vector<vector<int> > Solution::threeSum(vector<int> &A) {
    if(A.size() < 3)
        return {};
    vector<vector<int>> res;
    sort(A.begin(), A.end());
    long long sum = -1;
    int j, k;
    for(int i = 0; i < A.size() - 2; i++){
        j = i + 1;
        k = A.size() - 1;
        while(j < k){
            sum = (long long)A[i] + (long long)A[j] + (long long)A[k];
            if(sum < 0)
                j++;
            else if(sum > 0)
                k--;
            else{
                vector<int> v = {A[i], A[j], A[k]};
                sort(v.begin(), v.end());
                if(find(res.begin(), res.end(), v) == res.end())
                    res.push_back(v);
                j++;
                k--;
            }
        }
    }
    return res;
}