int Solution::solve(TreeNode* A) {
    queue<TreeNode*> tem1, tem2;
    TreeNode* node;
    int res = 0, temp=0;
    tem1.push(A);
    while(!tem1.empty()) {
        node = tem1.front();
        tem1.pop();
        temp += node -> val;
        if(node -> left)
            tem2.push(node->left);
        if(node->right)
            tem2.push(node->right);
        if(tem1.empty()) {
            res = max(res, temp);
            temp = 0;
            tem1.swap(tem2);
        }
    }
    return max(res, temp);
}