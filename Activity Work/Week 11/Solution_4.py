# Problem 4: Pacific Atlantic Water Flow

def pacificAtlantic(heights: list[list[int]]) -> list[list[int]]:
    """
    Finds cells from which water can flow to both oceans using two reverse DFS traversals.
    Time Complexity: O(m * n), Space Complexity: O(m * n).
    """
    if not heights or not heights[0]:
        return []

    m, n = len(heights), len(heights[0])
    
    # Tracking sets: Stores (r, c) tuples that can reach each ocean
    pacific_reachable = set()
    atlantic_reachable = set()

    # Directions for movement (North, South, East, West)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def dfs(r, c, reachable_set):
        """
        DFS traversal in reverse (water climbing up) to mark reachable cells.
        Water flows from a lower cell neighbor to a higher current cell.
        """
        if (r, c) in reachable_set:
            return
            
        reachable_set.add((r, c))

        # Check all 4 neighbors
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            # Check bounds and flow condition (water flows FROM neighbor TO current cell)
            if 0 <= nr < m and 0 <= nc < n:
                # If the neighbor is greater than or equal to the current cell (reverse flow)
                if heights[nr][nc] >= heights[r][c]: 
                    dfs(nr, nc, reachable_set)
                    
    # 1. Start DFS from Pacific Ocean edges (Top Row and Left Column)
    for c in range(n):
        dfs(0, c, pacific_reachable) # Top row
    for r in range(m):
        dfs(r, 0, pacific_reachable) # Left column

    # 2. Start DFS from Atlantic Ocean edges (Bottom Row and Right Column)
    for c in range(n):
        dfs(m - 1, c, atlantic_reachable) # Bottom row
    for r in range(m):
        dfs(r, n - 1, atlantic_reachable) # Right column
        
    # 3. Find the intersection of the two sets
    # Convert tuples (r, c) to list format [r, c] for the output
    result = [[r, c] for r, c in pacific_reachable if (r, c) in atlantic_reachable]
    
    return result

# --- Test Cases ---
# Example 1
heights1 = [
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4]
]
print("Example 1: Input Matrix (heights):")
for row in heights1:
    print(f"  {row}")
output1 = pacificAtlantic(heights1)
print(f"Example 1: Output: {output1}")
# Expected: [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (Order may vary)

# Example 2
heights2 = [[1]]
print(f"\nExample 2: Input: {heights2}")
output2 = pacificAtlantic(heights2)
print(f"Example 2: Output: {output2}")
# Expected: [[0, 0]]