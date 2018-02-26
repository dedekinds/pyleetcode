'''
692. Top K Frequent Words
2018.2.26
'''
  
#_________________________________________________________
import collections
class Solution(object):
    def topKFrequent(self, words, k):
        temp=collections.Counter(words)
        name=temp.keys()
        name.sort(key=lambda:x (-temp[x],x) )#如果tuple的第一项相同，那么按照第二项排列（此处为字典序）
        return name[:k]
        
    
import collections    
class Solution(object):
    #O(N+klog(N))
    def topKFrequent(self, words, k):
        count = collections.Counter(words)
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)#O(N)
        return [heapq.heappop(heap)[1] for x in range(k)]#pop→O(logN)
    
'''
(堆的操作Python)http://blog.csdn.net/u010480899/article/details/52863996

'''