int Solution::isValid(string A) {
    stack<char> st;
    map<char,char> tem;
    tem[')'] = '(';
    tem['}'] = '{';
    tem[']'] = '[';
    for(int i = 0; i < A.size(); i++) {
        if(A[i]=='(' || A[i]=='{' || A[i]=='[')
            st.push(A[i]);
        else if(!st.empty() && st.top() == tem[A[i]])
            st.pop();
        else
            return 0;
    }
    if(st.empty())
        return 1;
    return 0;
}