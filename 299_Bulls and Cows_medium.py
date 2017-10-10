'''
299. Bulls and Cows 
2017.10.10
'''
暴力+哈希 O(n)
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        d=dict()
        bulls=0
        total=0
        for x in secret:
            temp=int(x)
            if d.get(temp,-1)!=-1:
                d[temp]+=1
            else:
                d[temp]=1
        for x in range(0,len(guess)):
            if guess[x]==secret[x]:
                bulls+=1
            if d.get(int(guess[x]),-1)>0:
                d[int(guess[x])]-=1
                total+=1
        return str(bulls)+'A'+str(total-bulls)+'B'
                
_______________________________________________
class Solution(object):
    def getHint(self, secret, guess):
        bull = sum(i == j for i, j in zip(secret, guess))
        cow = sum(min(secret.count(x), guess.count(x)) for x in '0123456789')
        return '%dA%dB' % (bull, cow - bull)

x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]
xyz = zip(x, y, z)
print xyz
>>>[(1, 4, 7), (2, 5, 8), (3, 6, 9)]