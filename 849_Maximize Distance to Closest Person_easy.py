.
class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        seat_one_index = []
        for index in range(len(seats)):
            if seats[index]:
                seat_one_index.append(index)
        #print(seat_one_index)
        tempres = [-1]
        for i in range(len(seat_one_index)-1):
            tempres.append(int((seat_one_index[i+1]-seat_one_index[i])/2))
        return max(max(tempres),seat_one_index[0],len(seats)-seat_one_index[-1]-1)