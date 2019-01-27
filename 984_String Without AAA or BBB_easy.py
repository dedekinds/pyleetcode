class Solution(object):
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        if A>B:
            big = A
            small = B
            big_val = 'a'
            small_val = 'b'
        else:
            big = B
            small = A
            big_val = 'b'
            small_val = 'a'
            
        u_big = int(big/2)
        r_big = big%2
        u_small = int(small/(u_big+1))
        r_small = small % (u_big + 1)
        
        temp_small = [u_small]*(u_big+1)
        for i in range(r_small):
            temp_small[i] += 1
        
        ans = ''
        for i in range(u_big):
            ans += big_val*2
            ans += temp_small[i]*small_val
        ans += r_big * big_val
        ans += temp_small[-1] * small_val
        return ans