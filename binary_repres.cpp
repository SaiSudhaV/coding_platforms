int Solution::solve(int A) {
    if(A == 1)
        return 1;
    if(A == 2)
        return 3;
    bool order = true;
    int res = 0, count = 0, i = 1, j, k, t, p, tem;
    while(2 * (i - 1) < A) {
        i *= 2;
        count++;
    }
    t = i / 2;
    if(A - i + 2 > t)
        order = false;
    count = 1;
    while(A > 2) {
        p = 0;
        i = 1;
        while(2 * (i - 1) < A) {
            p++;
            i *= 2;
        }
        tem = (order ? (1 << 2 * (p - 1)) + 1 : (1 << 2 * p - 1) + 1) * count;
        res += tem;
        k = A - (order ? 0 : i / 2) - i + 1;
        p = 0;
        j = 1;
        while(j - 1 < k) {
            p++;
            j *= 2;
        }
        while(i != j){
            count *= 2;
            i /= 2;
        }
        A = i - 2 + (order ? 0 : i / 2) + (k - i / 2 + 1);
    }
    if(A == 1)
        res += count;
    if(A == 2)
        res += 3 * count;
    return res;
}