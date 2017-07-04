'''224. Basic Calculator 
   2017.7.4

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

def rowcheck(s):
    if s=='+':
        return 0
    if s=='-':
        return 1
    if s=='*':
        return 2
    if s=='/':
        return 3
    if s=='(':
        return 4
def colcheck(s):
        return rowcheck(s)

def charcheck(cal1,calchar,cal2):#四则运算
    if calchar=='+':
        return cal1+cal2
    if calchar=='-':
        return cal1-cal2
    if calchar=='*':
        return cal1*cal2
    if calchar=='/':
        return int(cal1/cal2)

class Solution(object):
    def calculate(self, s):
        #先建立优先级表
        #'+-*/()'、
                #0   1   2   3   4   
                #+   -   *   /   (   
        judge=[['>','>','<','<','<'],  #+  0
               ['>','>','<','<','<'],  #-  1
               ['>','>','>','>','<'],  #*  2
               ['>','>','<','<','<'],  #/  3
               ['<','<','<','<','<'],] #(  4、

        #初始化
        s_char=Stack()#存符号
        s_num=Stack()#存数字
        s_char.push('(')
        s=s+')'
        x=0
        while x<len(s):
            if s[x]==' ':
                x+=1
                continue
            if s[x] in ['0','1','2','3','4','5','6','7','8','9']:#如果是数码
                tempans=int(s[x])
                while True:#将两位以上的数码提取出来
                    if s[x+1] in ['0','1','2','3','4','5','6','7','8','9']:
                        tempans=tempans*10+int(s[x+1])
                        x+=1
                    else:
                        x+=1
                        break
                s_num.push(tempans)
                #print(x)
                #print(s_num.stackprint())
                continue
            else:#如果是字符的话  # ')'处理
                check=s_char.peek()
                #print(s_num.stackprint(),s_char.stackprint())
                if s[x]==')':#如果是右括号，要将到左括号之内的东西都搞完
                    while(s_char.peek()!='('):
                        cal2=s_num.pop()
                        cal1=s_num.pop()
                        calchar=s_char.pop()
                        s_num.push(charcheck(cal1,calchar,cal2))
                    s_char.pop()#弹出那个'('
                    x+=1
                    continue
                #print(check,s[x])

                if judge[rowcheck(check)][colcheck(s[x])]=='<':
                    s_char.push(s[x])
                    x+=1
                    continue
                else:#如果是‘>’,注意到这里全部是二元运算符
                    cal2=s_num.pop()
                    cal1=s_num.pop()
                    calchar=s_char.pop()#之前也许也有优先的字符
                    s_num.push(charcheck(cal1,calchar,cal2))
                    x+=1
                    continue
        return s_num.pop()  

                    
                           
s=" 3+5 / 2 "
temp=Solution()
print(temp.calculate(s))



