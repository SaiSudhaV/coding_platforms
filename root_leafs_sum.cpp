/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
void nodes_sum(TreeNode*, int, int &);
 
int Solution::sumNumbers(TreeNode* A) {
    int tem = 0;
    int res = 0;
    nodes_sum(A, tem, res);
    return res%1003;
}

void nodes_sum(TreeNode* A,int B,int &res){
    if(A == NULL)
        return;
    B = ((B * 10) % 1003 + A->val) % 1003;
    if(A -> left == NULL && A -> right == NULL) {
        res = (res + B) % 1003;
        return;
    }
    nodes_sum(A->right, B, res);
    nodes_sum(A->left, B, res);
}