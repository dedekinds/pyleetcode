class Solution(object):
    def isValid(self, S):
        """
        :type S: str
        :rtype: bool
        """
        check = dict()
        for temp in ['a','b','c']:
            check[temp] = 0
        stack = list(S)
        if len(stack) == 0:return False
        while stack:
            u = stack.pop()
            if u == 'c':
                check['b']+=1
            if u == 'b':
                check['b'] -= 1
                check['a'] += 1
                if check['b'] < 0:return False
            if u == 'a':
                check['a'] -= 1
                if check['a'] < 0:return False
        if check['a'] == 0 and check['b'] == 0:return True
        else:return False