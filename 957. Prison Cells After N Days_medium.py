找到这个一系列变换的循环点在哪里就可以了，实际上这个变换在常数循环上就能得到循环？基于这个事实
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
