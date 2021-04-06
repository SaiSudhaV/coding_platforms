minWindow(string A, string B) {
    int n = A.length(), m = B.length(), c[256] = {}, temp[256] = {};
    for(int i = 0; i < m; i++)
        c[B[i] - '0']++;
    int count = 0, s = 0, t, idx = n + 1;    
    for(int i = 0; i < n; i++) {
        temp[A[i] - '0']++;
        if(c[A[i] - '0'] != 0 && c[A[i] - '0'] >= temp[A[i] - '0'])
            count += 1;
        if(count == m) {
            while(temp[A[s] - '0'] > c[A[s] - '0'] || c[A[s] - '0'] == 0){
                if(temp[A[s] - '0'] > c[A[s] - '0'])
                    temp[A[s] - '0'] -= 1;
                s += 1;
            }
            if(i - s + 1 < idx) {
                t = s;
                idx = i - s + 1;
            }
            count -= 1;
            temp[A[s] - '0'] -= 1;
            s += 1;
        }
    }
    
    if(idx == n + 1)
        return "";
    return A.substr(t, idx);
}