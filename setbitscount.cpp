long long is_lsb_set(long long);
long long set_bits_count(long long);

int Solution::solve(int A) {
    return set_bits_count(A) % 1000000007;
} 

long long is_lsb_set(long long n) {
    int res = 0;
    while(n > 1)  {
        n >>= 1;
        res++;
    }
    return res;
}

long long set_bits_count(long long n) {
    long long m;
    if(n == 0)
        return 0;
    m = is_lsb_set(n);
    if(n == ((1 << (m + 1)) - 1))
        return ((m + 1)*(1 << m));
    n -= (1 << m);
    m *= 1 << (m - 1);
    return n + 1 + m + set_bits_count(n);  
}