264的推广ugly number

class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        pri_index = [0]*len(primes)
        uglynum = [1]
        for i in range(n - 1):
            nextugly = min(uglynum[pri_index[tmp]]*primes[tmp] for tmp in range(len(primes)))
            uglynum.append(nextugly)
            for i in range(len(primes)):
                #print('next',nextugly)
                #print(primes[i])
                if nextugly % primes[i] == 0:
                    pri_index[i] += 1
        return uglynum[-1]