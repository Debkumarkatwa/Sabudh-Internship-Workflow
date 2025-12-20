# Problem 5: Rotting Oranges

from collections import deque

def orangesRotting(grid: list[list[int]]) -> int:
    """
    Calculates the minimum time for all fresh oranges to rot using Multi-Source BFS.
    Time Complexity: O(m * n), Space Complexity: O(m * n).
    """
    if not grid:
        return 0

    m, n = len(grid), len(grid[0])
    queue = deque() # Stores [(r, c, time)]
    fresh_count = 0
    max_time = 0

    # 1. Initialize queue with all initial rotten oranges (sources) and count fresh ones
    for r in range(m):
        for c in range(n):
            if grid[r][c] == 2:
                queue.append((r, c, 0)) # Store (row, col, time)
            elif grid[r][c] == 1:
                fresh_count += 1
                
    # If no fresh oranges exist initially, return 0
    if fresh_count == 0:
        return 0

    # Directions for 4-directional adjacency
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # 2. BFS Simulation
    while queue:
        r, c, time = queue.popleft()
        max_time = max(max_time, time)

        # Check all 4 neighbors
        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            # Check bounds and if the neighbor is a fresh orange (1)
            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                # Rot the fresh orange
                grid[nr][nc] = 2
                fresh_count -= 1
                
                # Add the newly rotten orange to the queue for the next minute
                queue.append((nr, nc, time + 1))

    # 3. Final Result
    # If fresh_count is 0, the process succeeded, return the max time recorded.
    # Otherwise, some fresh oranges remain (impossible to rot), return -1.
    return max_time if fresh_count == 0 else -1

# --- Test Cases ---
# Example 1
grid1 = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
output1 = orangesRotting(grid1)
print(f"Example 1: Input: {grid1} | Output: {output1}")
# Expected: 4

# Example 2
grid2 = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
output2 = orangesRotting(grid2)
print(f"Example 2: Input: {grid2} | Output: {output2}")
# Expected: -1

# Example 3
grid3 = [[0, 2]]
output3 = orangesRotting(grid3)
print(f"Example 3: Input: {grid3} | Output: {output3}")
# Expected: 0