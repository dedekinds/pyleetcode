'''593. Valid Square 
   2017.8.21
'''
#思路是判断对角线是否垂直，对角线交点和邻近顶点是否距离相等即可
#小心p1,p2..p4是没有顺序的
#小心可能退化成三角形或以下
class Solution(object):
    def validSquare(self, p1, p2, p3, p4):

        tempset=[p1,p2,p3,p4]#小心可能退化成三角形或以下，处理退化情况
        for x in range(len(tempset)):
            for y in range(x+1,4):
                if tempset[x]==tempset[y]:
                    return False

        mid1_2=[(p1[0]+p2[0])/2.0,(p1[1]+p2[1])/2.0]
        mid3_4=[(p3[0]+p4[0])/2.0,(p3[1]+p4[1])/2.0]
        mid1_3=[(p3[0]+p1[0])/2.0,(p3[1]+p1[1])/2.0]
        mid2_4=[(p2[0]+p4[0])/2.0,(p2[1]+p4[1])/2.0]
        
        #处理pi的次序问题，统一成1-2,3-4相对的情况
        if (mid1_2 !=mid3_4) and (mid1_3==mid2_4):
            temp=p2
            p2=p3
            p3=temp
        elif (mid1_2 !=mid3_4) and (mid1_3!=mid2_4):
            temp=p2
            p2=p4
            p4=temp
        #1.原来p1,p2..p4是没有顺序的
        #2.这里为什么x/2不行，需要x/2.0和本地测试不同，不过没关系
        #下面的程序是1-2,3-4相对的情况：只需要把情况转换为这种就行了
        v1=[p2[0]-p1[0],p2[1]-p1[1]]
        v2=[p3[0]-p4[0],p3[1]-p4[1]]
        mid=[(p1[0]+p2[0])/2.0,(p1[1]+p2[1])/2.0]
        
        A=((v1[0]*v2[0]+v1[1]*v2[1])==0)
        dis1=(mid[0]-p1[0])*(mid[0]-p1[0])+(mid[1]-p1[1])*(mid[1]-p1[1])
        dis2=(mid[0]-p3[0])*(mid[0]-p3[0])+(mid[1]-p3[1])*(mid[1]-p3[1])
        B=(dis1==dis2)

        return A and B