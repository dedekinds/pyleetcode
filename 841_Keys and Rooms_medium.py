class Solution:
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        if len(rooms) == 0:return True
        n = len(rooms)
        visited = [1]*n
        
        stack = [0]
        
        while stack:
            temp = stack.pop()
            if visited[temp]:
                stack += rooms[temp]
                visited[temp] = 0
        return sum(visited) == 0