class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
        
        visited = [0] * numCourses
        
        def dfs(course):
            if visited[course] == 1:
                return False  # cycle found
            
            if visited[course] == 2:
                return True   # already completed
            
            visited[course] = 1
            
            for next_course in graph[course]:
                if not dfs(next_course):
                    return False
            
            visited[course] = 2
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True