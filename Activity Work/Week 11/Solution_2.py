# Problem 2: Course Schedule

from collections import deque

def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    """
    Checks if all courses can be finished by detecting cycles using Kahn's algorithm (BFS).
    Time Complexity: O(V + E), Space Complexity: O(V + E).
    """
    # 1. Initialize Adjacency List (graph) and In-degrees (number of prerequisites)
    # The graph stores: course_i -> list_of_courses_that_require_course_i
    adj = {i: [] for i in range(numCourses)}
    in_degree = [0] * numCourses

    # Build graph and in-degrees
    for course, prereq in prerequisites:
        # Prereq -> Course (Edge direction)
        adj[prereq].append(course)
        in_degree[course] += 1

    # 2. Initialize Queue with courses having an in-degree of 0 (no prerequisites)
    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])

    courses_taken = 0

    # 3. BFS (Topological Sort)
    while queue:
        prereq_course = queue.popleft()
        courses_taken += 1

        # For all courses that require the current prerequisite
        for course in adj[prereq_course]:
            # Decrease the in-degree of the dependent course
            in_degree[course] -= 1
            
            # If a course now has zero prerequisites, it can be taken (added to queue)
            if in_degree[course] == 0:
                queue.append(course)

    # If the number of courses taken equals the total number of courses, 
    # then no cycle exists, and all courses can be finished.
    return courses_taken == numCourses

# --- Test Cases ---
# Example 1
numCourses1 = 2
prerequisites1 = [[1, 0]]
output1 = canFinish(numCourses1, prerequisites1)
print(f"Example 1: Input: {numCourses1}, {prerequisites1} | Output: {output1}")
# Expected: True (Course 0 -> Course 1)

# Example 2
numCourses2 = 2
prerequisites2 = [[1, 0], [0, 1]]
output2 = canFinish(numCourses2, prerequisites2)
print(f"Example 2: Input: {numCourses2}, {prerequisites2} | Output: {output2}")
# Expected: False (Cycle: Course 0 <-> Course 1)