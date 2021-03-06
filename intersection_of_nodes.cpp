/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
ListNode* Solution::getIntersectionNode(ListNode* A, ListNode* B) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details
    set <ListNode*> tempNode;
    while(A != NULL) {
        tempNode.insert(A);
        A = A -> next;
    }
    while(B != NULL) {
        if(tempNode.find(B) != tempNode.end())
           return B;
        B = B -> next;
    }
    return NULL;
}

