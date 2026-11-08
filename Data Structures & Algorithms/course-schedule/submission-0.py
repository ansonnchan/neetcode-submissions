class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        #cyclic detection -> if there is a conflict, there will be a cycle

        #map each course to prereqs
        prereqMap = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            prereqMap[course].append(prereq)
        
        #store all visited courses along a current path
        visited = set()

        def dfs(course):
            if course in visited: #then a cycle
                return False
            
            if prereqMap[course] == []: 
                return True
            
            visited.add(course)

            for prereq in prereqMap[course]:
                if not dfs(prereq):
                    return False
            
            visited.remove(course)
            prereqMap[course] = []

            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True



