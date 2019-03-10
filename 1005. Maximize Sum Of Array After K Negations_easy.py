class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        temp = sorted(A)
        s = 0
        negt = 0
        for i in range(len(temp)):
            if temp[i] <= 0:
                negt += 1
            else:
                break
        minneg = temp[i-1]
        if negt == 0:
            return sum(temp) - temp[0] + (-1)**(K%2) * temp[0]
        elif K <= negt:
            for i in range(len(A)):
                if K:
                    s += (-1)*temp[i]
                    K -= 1
                else:
                    s += temp[i]
            return s
        elif K > negt:
            r = []
            for i in range(len(A)):
                r.append(abs(A[i]))
            check = sorted(r)
            tt = K - negt
            s = sum(check)
            s -= check[0]
            s += (-1)**(tt)*check[0]
            return s
                
            