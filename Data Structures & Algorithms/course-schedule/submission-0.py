from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Return True if you can finish all courses given the list of prerequisites,
        otherwise False. Detects cycles in the prerequisite graph via DFS.
        """
        if numCourses <= 0:
            return False

        # Build adjacency list: course_id → list of its prerequisite course_ids
        prereq_graph: List[List[int]] = [[] for _ in range(numCourses)]
        for course_id, prereq_id in prerequisites:
            prereq_graph[course_id].append(prereq_id)

        completed: set[int] = set()   # courses fully processed (no cycles downstream)
        visiting: set[int] = set()    # courses in the current DFS recursion stack
        can_finish: bool = True       # global flag—set False if we detect a cycle

        def dfs_visit(course_id: int) -> None:
            nonlocal can_finish
            if not can_finish:
                return

            # cycle if we see a node already on the recursion stack
            if course_id in visiting:
                can_finish = False
                return

            # already checked this course and its prerequisites
            if course_id in completed:
                return

            # mark as visiting and recurse on prerequisites
            visiting.add(course_id)
            for prereq_id in prereq_graph[course_id]:
                dfs_visit(prereq_id)
                if not can_finish:
                    return
            visiting.remove(course_id)

            # mark as completed—no cycles found in its subtree
            completed.add(course_id)

        # Launch DFS from every course (to cover disconnected components)
        for course_id in range(numCourses):
            if not can_finish:
                break
            if course_id not in completed:
                dfs_visit(course_id)

        return can_finish
