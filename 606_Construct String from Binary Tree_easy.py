'''606. Construct String from Binary Tree 
   2017.7.25

'''
class Stack(object): 
    def __init__(self): #建立栈
        self.items = [] 
    def isEmpty(self): 
        return len(self.items)==0#判断是否为空  
    def push(self, item): 
        self.items.append(item)#压栈
    def pop(self): 
        return self.items.pop()#出栈  
    def peek(self): 
        if not self.isEmpty(): #取出顶端栈
            return self.items[len(self.items)-1] 
    def size(self): 
        return len(self.items)#长度
    def stackprint(self):
        return self.items

class Solution(object):
    def tree2str(self, t):
        #用栈的思路去做，放')' tree.val '('
        ans=''
        if t==None:
            return ans
        s=Stack()
        s.push(')')
        s.push(t)
        s.push('(')
        while s.isEmpty()!=True:
            temp=s.pop()
            #print(s.stackprint())
            if temp=='(' or temp==')':
                ans+=temp
                #continue
            else:
                ans+=str(temp.val)
                if temp.left or temp.right:
                    if temp.right:
                        s.push(')')
                        s.push(temp.right)
                        s.push('(')
                    s.push(')')
                    if temp.left:
                        s.push(temp.left)
                    s.push('(')

                #continue
        return ans[1:-1]

                


_____________________
递归的思路！
class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t: return ''
        ans = str(t.val)
        if t.left or t.right: ans += '(' + self.tree2str(t.left) + ')'
        if t.right: ans += '(' + self.tree2str(t.right) + ')'
        return ans

        
        
        
        
        
