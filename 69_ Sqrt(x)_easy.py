'''69. Sqrt(x) 
   2017.7.3

'''
class Solution(object):
    def mySqrt(self, x):
        ans=1
        while True:
            temp=0.5*(ans+x/ans)
            if abs(temp-ans)<0.1:
                return int(temp)
            else:
                ans=temp

————————————————————————
二分
public int sqrt(int x) {
    if (x == 0)
        return 0;
    int left = 1, right = Integer.MAX_VALUE;
    while (true) {
        int mid = left + (right - left)/2;
        if (mid > x/mid) {
            right = mid - 1;
        } else {
            if (mid + 1 > x/(mid + 1))
                return mid;
            left = mid + 1;
        }
    }
}