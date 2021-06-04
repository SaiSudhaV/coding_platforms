long long int power(long long int, long long int);
bool compare(pair<int, long long int> , pair<int, long long int>);
void calculate();

long long int ar[100005];

vector<int> Solution::solve(vector<int> &A, vector<int> &B) {
    calculate();
    int n = (int)A.size();
    long long int l[n], r[n], p[n];
    for(int i = 0; i < n; i += 1) {
        l[i] = r[i] = 1;
    }
    for(int i = 1; i < n; i += 1) {
        int last = i-1;
        while(last >= 0 and A[i] > A[last]) {
            l[i] += l[last];
            last -= l[last];
        }
    }
    for(int i = n-2; i >= 0; i -= 1) {
        int last = i+1;
        while(last < n and A[i] >= A[last]) {
            r[i] += r[last];
            last += r[last];
        }
    }
    for(int i = 0; i < n; i += 1) {
        p[i] = l[i] * r[i];
    }
    pair<int, long long int> tem[n];
    for(int i = 0; i < n; i += 1) {
        tem[i] = {ar[A[i]], p[i]};
    }
    sort(tem, tem + n, compare);
    long long ptr[n];
    ptr[0] = tem[0].second;
    for(int i = 1; i < n; i += 1) {
        ptr[i] = ptr[i-1] + tem[i].second;
    }
    int q = (int)B.size();
    vector<int> ans(q);
    for(int i = 0; i < q; i += 1) {
        auto id = lower_bound(ptr, ptr + n, B[i]) - ptr;
        ans[i] = tem[id].first;
    }
    return ans;
}

long long int power(long long int A, long long int B) {
    long long int res = 1;
    while(B){
        if(B & 1)
            res = (res % 1000000007 * A % 1000000007) % 1000000007;
        A = (A % 1000000007 * A % 1000000007) % 1000000007;
        B >>= 1;
    }
    return res;
}

void calculate() {
    ar[0] = 0;
    ar[1] = 1;
    if(ar[2] != 0)
        return;
    for(long long int i = 2; i < 100005; i += 1)
        if(ar[i] == 0) {
            ar[i] = 2;
            for(long long int j = i + i; j < 100005; j += i) {
                if(ar[j] == 0) ar[j] = 1;
                long long int tem = j, count = 0;
                while(tem % i == 0) {
                    tem /= i;
                    count++;
                }
                ar[j] *= (count + 1);
            }
        }
    for(int i = 2; i < 100005; i += 1) {
        ar[i] = (power(i, ar[i] / 2) % 1000000007 * (ar[i] & 1 ? (long long int)sqrt(i) : 1)%1000000007)%1000000007;
    }
}

bool compare(pair<int, long long int> A, pair<int, long long int> B) {
    if(A.first != B.first)
        return A.first > B.first;
    else
        return A.second < B.second;
}