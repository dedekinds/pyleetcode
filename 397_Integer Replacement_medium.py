'''397. Integer Replacement 
   2017.8.8
'''

class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        #直接用递归，本来想着用动态规划的（希望N不要太大），O(logn)
        if n==1:return 0
        if n%2==0:return self.integerReplacement(n/2)+1
        return min(self.integerReplacement(n+1),self.integerReplacement(n-1))+1
        
        
%之前猜想 4k+1 4k+3决定了是n-1还是n+1，似乎是对的？（3是唯一反例

————————————————————————————————————————————————————————————
解法II 位运算（Bit Manipulation）

参考LeetCode Discuss，链接地址：https://discuss.leetcode.com/topic/58334/a-couple-of-java-solutions-with-explanations/

该解法采用迭代方式求解。

当n为偶数时，下一次迭代n的取值确定为n / 2；
当n为奇数时，下一次迭代n的取值n + 1或者n - 1，由其二进制表示中的最低两位数决定：
若n的最低两位数为01，则令n = n - 1
否则，若n的最低两位数为11，则令n = n + 1

这样处理是为了使n的二进制表式中1的数目尽可能少，从而减少迭代次数
需要注意的是，当n = 3时，不满足上述判定条件，需要单独处理。

___________________________
一种BFS的想法：C++
class Solution {
public:
    int integerReplacement(int n) {
        int res = 0;
        queue<long long> q;
        q.push(n);
        while(!q.empty()){
            int n = q.size();
            for(int i = 0; i < n; i++){
                long long x = q.front();
                q.pop();
                if(x == 1) return res;
                if(x % 2 == 0) q.push(x / 2);
                else{
                    q.push(x + 1);
                    q.push(x - 1);
                }
            }
            res++;
        }
        return res;
    }
};