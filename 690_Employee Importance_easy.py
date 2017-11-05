'''
690. Employee Importance
2017.11.5
'''
"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
先建立一个索引，如果employee是纯数组就好了
然后就用简单地递归就可以完成了
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        temp={emp.id:emp for emp in employees}#先建立一个索引
        #定义一个递归
        def temp_ans(id):
            if id is None:
                return None
            target=temp[id]
            return target.importance + sum(temp_ans(temp_id) for temp_id in target.subordinates)
        return temp_ans(id)
