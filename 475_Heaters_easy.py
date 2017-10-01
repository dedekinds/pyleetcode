'''475. Heaters 
   2017.10.1
'''
1.先找到对于每一个house的最小覆盖半径：
对每一个house在heaters中找左右界，然后不断更新【二分选择bisect模块】
2.每次寻找都更新最后的最小半径，取最大即可（因为都要覆盖


import bisect
class Solution(object):
    def findRadius(self, houses, heaters):
        heaters.sort()
        ans=0
        for temp in houses:
            now_ans=pow(10,9)+1
            le=bisect.bisect_right(heaters,temp)#找一个不大于房子的供暖站
            if le>0:
                now_ans=min(now_ans,abs(heaters[le-1]-temp))
            ge=bisect.bisect_left(heaters,temp)#找一个不小于房子的供暖站
            if ge<len(heaters):
                now_ans=min(now_ans,abs(heaters[ge]-temp))
            #print(temp,now_ans)
            #上面是对于每一个hourse找个最小的覆盖半径
            #下面的max是为了找一个全局都能覆盖的，所以是取最大咯
            ans=max(ans,now_ans)
        return ans
