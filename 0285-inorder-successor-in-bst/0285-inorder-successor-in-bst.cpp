/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* inorderSuccessor(TreeNode* root, TreeNode* p) {
        if(p == nullptr)
            return p;
        TreeNode *node = root, *parent = nullptr;
        while(node && node != p){
            if(node->val < p->val){
                node = node->right;
            }
            else{
                parent = node;
                node = node->left;
            }
        }
        if(node == nullptr)
            return node;
        
        if(node->right){
            node = node->right;
            while(node->left)
                node = node->left;
            return node;
        }
        
        return parent;
    }
};