'''20. Valid Parentheses 
   2017.7.2

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

#利用栈，当右括号的时候全部入栈，但左括号的时候，判断栈顶是否匹配，若不匹配就FALSE，若
#匹配就出栈，最后判断栈是否为空即可   
class Solution(object):
    def isValid(self, s):
        temp=Stack()
        for x in range(len(s)):
            #print(temp.stackprint())
            if s[x]=='{' or s[x]=='(' or s[x]=='[':   
                temp.push(s[x])
                continue
            if s[x]=='}' and temp.peek()=='{':
                temp.pop()
                continue
            if s[x]==']' and temp.peek()=='[':
                temp.pop()
                continue
            if s[x]==')' and temp.peek()=='(':
                temp.pop()
                continue
            else:
                return False
        return temp.isEmpty()

                               
s='[([{}])]'
temp=Solution()
print(temp.isValid(s))



