'''
777. Swap Adjacent in LR String
2018.2.4
'''
class Solution:
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        #一共有两点
        #第一根据题目暗示，R只能走右边，L只能走左边，所以两个子串的RL的相对位置要一样（即去掉X之后）
        #start的R的index要比end的R要小，L类似
        
        start_index=[(i,string) for i,string in enumerate(start) if string!='X']
        end_index=[(i,string) for i,string in enumerate(end) if string!='X']
        
        if len(start_index)!=len(end_index):return False
        
        for temp in range(len(start_index)):
            Num,Str=start_index[temp]
            NUM,STR=end_index[temp]
            
            if Str=='R' and STR=='R':
                if Num<=NUM:
                    continue
                else:
                    return False
            if Str=='L' and STR=='L':
                if Num>=NUM:
                    continue
                else:
                    return False
            else:
                return False
        return True
            
            