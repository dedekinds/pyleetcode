'''617. Merge Two Binary Trees 
   2017.7.25

'''
#思路先是计算高度，然后层次遍历
def height(tree):
    if tree==None:
        return 0
    return max(height(tree.left),height(tree.right))+1

class Solution(object):
    def mergeTrees(self, t1, t2):
        tree_height=max(height(t1),height(t2))
            #解决空树的情况
        if tree_height==0:
            return t1#反正都是空树
                #开始进行层次遍历
        #解决特殊情况
        if t1==None and t2:
        	return t2
        if t2==None and t1:
        	return t1
        Q1=[t1]
        Q2=[t2]
        while tree_height:
            tree_height-=1
            tempQ1=[]
            tempQ2=[]
            for x in range(len(Q1)):
                Q1[x].val=Q1[x].val+Q2[x].val
                
                if Q1[x].left or Q2[x].left:
                    if Q1[x].left:
                        tempQ1.append(Q1[x].left)
                    elif tree_height!=0:
                        Q1[x].left=TreeNode(0)
                        tempQ1.append(Q1[x].left)
                    if Q2[x].left:
                        tempQ2.append(Q2[x].left)
                    elif tree_height!=0:
                        Q2[x].left=TreeNode(0)
                        tempQ2.append(Q2[x].left)    
                        
                if Q1[x].right or Q2[x].right:
                    if Q1[x].right:
                        tempQ1.append(Q1[x].right)
                    elif tree_height!=0:
                        Q1[x].right=TreeNode(0)
                        tempQ1.append(Q1[x].right)
                    if Q2[x].right:
                        tempQ2.append(Q2[x].right)
                    elif tree_height!=0:
                        Q2[x].right=TreeNode(0)
                        tempQ2.append(Q2[x].right)                        
            Q1=tempQ1
            Q2=tempQ2
        return t1

采用了类似637. Average of Levels in Binary Tree 的方法
       

_________________________________________

class Solution(object):
    def mergeTrees(self, t1, t2):
        if (t1 is None) and (t2 is None):
            return None
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        
        t1.val = t1.val + t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1