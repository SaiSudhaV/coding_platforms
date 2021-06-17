/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
 
int validSymmetric(TreeNode*, TreeNode*);

int Solution::isSymmetric(TreeNode* A) {
    return validSymmetric(A -> left, A -> right);
}

int validSymmetric(TreeNode* l,TreeNode* r) {
    if (l == NULL && r == NULL)
        return 1;
    if (l == NULL || r == NULL)
        return 0;
    if (l -> val != r -> val)
        return 0;
    return validSymmetric(l -> left, r -> right) && validSymmetric(l -> right, r -> left);
}