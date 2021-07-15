vector<int> Solution::findSubstring(string A, const vector<string> &B) {
    vector<int> res;
    if(B.size() == 0)
        return res;
    int tem = B[0].size();
    if(tem == 0)
        return res;
    unordered_map<string, int> mp;
    for(auto i : B)
        mp[i] += 1;
    int i, j, p;
    for(i = 0; i < A.size(); i++){
        p = 0;
        j = i;
        while(mp[A.substr(j, tem)]){
            mp[A.substr(j, tem)] -= 1;
            p++;
            if(B.size() == p){
                res.push_back(i);
                break;
            }
            j += tem;
        }
        j = i;
        while(p--){
            mp[A.substr(j, tem)]++;
            j += tem;
        }
    }
    return res;
}