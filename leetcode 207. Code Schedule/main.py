from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # creating a graph
        graph = [ [] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        visit = [0] * numCourses

        def graph_dfs(course):
            # if there is a cyclic iteration.
            if visit[course] == 1:
                return False
            # if there is
            if visit[course] == 2:
                return True

            visit[course] = 1  # Mark as visiting
            for prereq in graph[course]:
                if not graph_dfs(prereq):
                    return False
            visit[course] = 2  # Mark as visited
            return True

        # Check each course to see if we can complete it
        for course in range(numCourses):
            if not graph_dfs(course):
                return False  # Cycle detected
        return True