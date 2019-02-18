迷之贪心策略通过...汗水
Python超时 C++通过GG垃圾
class Solution {
public:
    int minKBitFlips(vector<int>& A, int K) {
        int length = A.size();
        int res = 0;
        for (int i=0; i<length; i++){
            if(A[i] == 0){
                res += 1;
                for (int j=i;j < i+K; j++){
                    if (j >= length)return -1;
                    A[j] ^= 1;
                }
            }
        }
        return res;
    }
};


——————————————————————————————————————————————————————————————
BFS  TLE
class Solution(object):
    def minKBitFlips(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A = tuple(A)
        vis = set()
        Q = [A]
        vis.add(A)
        cnt = 0 
        length = len(A)
        target = tuple([1] * length)
        if A == target:
            return 0
        while Q:
            tempQ = []
            flag = False
            #print(Q)
            #u = Q.pop(0)
            #print(length-K+1)
            for u in Q:
                for i in range(length-K+1):
                    tmp = u[:]
                    #print(tmp[i:i+K])
                    check = tmp[i:i+K]
                    temp_ans = []
                    for j in range(len(check)):
                        if check[j] == 1:temp_ans.append(0)
                        if check[j] == 0:temp_ans.append(1)
                    res = tmp[:i] + tuple(temp_ans) +tmp[i+K:]
                    if res == target:
                        return cnt + 1
                    #print(res)
                    if res not in vis:
                        vis.add(res)
                        flag = True
                        tempQ.append(res)
            if flag:
                cnt += 1
            Q = tempQ
        return -1
                