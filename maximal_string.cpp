void maximal_string(string, int, int);

string res;

string Solution::solve(string A, int B) {
    res = A;
    maximal_string(A, B, 0);
    return res;
}

void maximal_string(string A, int B, int pos) {
    if(B == 0)
        return;
    for(int i = pos; i < A.size(); i++) {
        for(int j = i; j < A.size(); j++) {
            swap(A[i], A[j]);
            if(A >= res)
                res=A;
            maximal_string(A, B - 1, pos + 1);
            swap(A[i], A[j]);
        }
    }
}