'''
735. Asteroid Collision
2018.3.1
'''

class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        #http://blog.csdn.net/magicbean2/article/details/79413413
        ans=[]
        for x in asteroids:
            while ans and ans[-1]>0 and ans[-1]+x<0:
                ans.pop()
            if not ans or ans[-1]<0 or x>0:
                ans.append(x)
            elif ans[-1]>0 and ans[-1]+x==0:
                ans.pop()
        return ans