class Solution {
public:
    int TreeDepth(TreeNode* pRoot)
    {
        if (pRoot == nullptr)
            return 0;
        int nleft = TreeDepth(pRoot->left);
        int nright = TreeDepth(pRoot->right);
        return (nleft > nright)? nleft+1 :nright+1;
    }
};