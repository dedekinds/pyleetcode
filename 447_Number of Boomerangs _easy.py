'''447. Number of Boomerangs 
   2017.6.9

'''
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        #首先想到的是暴力，显然首先走早所有距离，至少是O(N^2)
        #或者先选两个，然后逐个遍历？这是O(n3)的猜测是过不了
        #想起那个k-means速度很快的办法


        #似乎O(n2)是可以的
        #拿一个字典，相当于是哈希了。首先遍历所有点，假设选取一个点A，那么遍历其所有距离（此时为O(N2)）,用字典来存距离
        #如果原本有就+1，没有就变成1，把每一次的排列组合都算出来即可
        sum1=0
        for i in range(len(points)):
            sumtemp=0
            dis=dict()
            for j in range(len(points)):
                d=(points[i][0]-points[j][0])**2+(points[i][1]-points[j][1])**2
                if d in dis and d!=0:
                    dis[d]+=1
                else:
                    dis[d]=1
            for a in dis.values():
                sumtemp+=a*(a-1)
            sum1+=sumtemp
        return sum1


'''
比较好的写法是这样：
res = 0
        for p in points:
            cmap = {}
            for q in points:
                f = p[0]-q[0]
                s = p[1]-q[1]
                cmap[f*f + s*s] = 1 + cmap.get(f*f + s*s, 0)
            for k in cmap:
                res += cmap[k] * (cmap[k] -1)
        return res

'''