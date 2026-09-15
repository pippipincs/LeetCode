class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        def dfs(room):
            visited.add(room)
            for nei in rooms[room]:
                if nei not in visited:
                    dfs(nei)
        dfs(0)
        return True if len(visited) == len(rooms) else False