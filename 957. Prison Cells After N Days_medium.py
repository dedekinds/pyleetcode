找到这个一系列变换的循环点在哪里就可以了，实际上这个变换在常数循环上就能得到循环？基于这个事实
实际上样本空间只有2^6=64种，抽屉原理循环才对（首尾两个为0

以5为例，我们可以得到一个mod2的线性系统，变换对应的矩阵为
[
0 0 0 0 0
1 0 1 0 0
0 1 0 1 0
0 0 1 0 1
0 0 0 0 0
]
如果不从抽屉原理，毕竟这和变换没什么关系，如果从变换角度入手呢，为何14次循环内必定会成环
一般线性空间中 A^k = k * A

奇怪，这个时候的线性运算中的+运算要变为异或运算，异或也满足结合律和交换律，再想想
好像也不对，除非0和任何数相乘都消失【也不对呐，这里矩阵起到的作用只是取数】
至少

a0 = 0
a1 = a0^a2
a2 = a1^a3
a3 = a2^a4
a4 = 0
这个是对的


循环节的可能情况
0 : [1]
1 : [1]
2 : [1]
3 : [1]
4 : [1, 2]
5 : [1]
6 : [1, 3, 6]
7 : [1, 2, 4]
8 : [1, 7, 14]
9 : [1]
10 : [1, 2, 7, 14]
11 : [1, 3, 6, 12]
12 : [1, 31, 62]
13 : [1, 2, 4, 8]
14 : [1, 63, 126]
15 : [1, 7, 14, 28]
16 : [1, 2, 3, 6, 15, 30]
17 : [1]
18 : [1, 5, 10, 15, 30]
19 : [1, 2, 4, 7, 14, 28]
数值计算了一下，第一个数是维度，本题为8

————————————————————————————————————————————————
class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        ans = [cells]
        index_target = 0
        max_loop = 20
        for i in range(1,max_loop):
            temp_ans = []
            for tmp in range(8):
                if tmp == 0 or tmp == 7:
                    temp_ans.append(0)
                elif cells[tmp-1]^cells[tmp+1] == 0:
                    temp_ans.append(1)
                else:
                    temp_ans.append(0)
            if temp_ans in ans:
                index_target = ans.index(temp_ans)
                break
            cells = temp_ans
            ans.append(cells)
        
        circle = len(ans) - index_target
        return ans[index_target + (N-index_target)%circle]
