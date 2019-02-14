反过来思考，最好一直除2，如果一旦低于显然只能一直+1

class Solution(object):
    def brokenCalc(self, X, Y):
        """
        :type X: int
        :type Y: int
        :rtype: int
        """
        res = 0
        while Y > X:
            if Y%2 == 0:
                Y = int(Y/2)
                res += 1
                if Y == X:break
            else:
                Y = Y+1
                res += 1
                if Y == X:break
        res += X - Y
        return res