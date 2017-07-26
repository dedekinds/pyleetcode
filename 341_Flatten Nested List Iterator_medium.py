'''341. Flatten Nested List Iterator 
   2017.7.25

'''
压平一个嵌套数组
[[1,1],2,[1,1]]→[1,1,2,1,1]


方法1：
>>> from functools import reduce
>>> c=reduce(lambda x,y:x+y, a)


方法2：
sum(a,[])即可