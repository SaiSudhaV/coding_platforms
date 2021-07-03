int Solution::solve(TreeNode* A) {
    queue<TreeNode*> tem1, tem2;
    int m = 0, temp=0;
    tem1.push(A);
    while(!tem1.empty()) {
        TreeNode* node = tem1.front();
        tem1.pop();
        temp += node -> val;
        
        if(node -> left)
            tem2.push(node->left);
        if(node->right)
            tem2.push(node->right);
        
        if(tem1.empty()) {
            tem1.swap(t);
            m = max(m, temp);
            temp = 0;
        }
    }
    return max(m, temp);
}