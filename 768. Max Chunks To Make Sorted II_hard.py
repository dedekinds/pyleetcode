class Solution:
    def maxChunksToSorted(self, arr: 'List[int]') -> 'int':
        sum_pre = 0
        sum_cur = 0
        sort_arr = sorted(arr)
        ans = 0
        for i in range(len(arr)):
            sum_pre += arr[i]
            sum_cur += sort_arr[i]
            if sum_pre == sum_cur:
                sum_pre = 0
                sum_cur = 0
                ans += 1
        return ans