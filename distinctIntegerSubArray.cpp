int Solution::solve(vector<int> &A, int B) {
    int result = 0, temp = 0, count = 0, j = 0, n = A.size();
    unordered_map<int, int> countArray;
    for(int i = 0; i < n; ++i) {
        if (countArray[A[i]]++ == 0) 
            ++count;
        if (count > B){
            temp = 0;
            --count;
            --countArray[A[j++]];
        }
        while (countArray[A[j]] > 1){
            ++temp;
            --countArray[A[j++]];
        }
        if (count == B) 
            result = result + temp + 1;
    }
    return result;
}