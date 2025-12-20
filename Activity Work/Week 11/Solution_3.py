# Problem 3: Binary Tree Zigzag Level Order Traversal

from collections import deque

class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Helper function to simulate tree building from list input
def build_tree_from_list(values):
    """Builds a tree using a level-order representation (like LeetCode)."""
    if not values:
        return None
        
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        node = queue.popleft()
        
        # Left child
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        # Right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
        
    return root

def zigzagLevelOrder(root: TreeNode) -> list[list[int]]:
    """
    Performs BFS level order traversal with direction alternating (zigzag).
    Time Complexity: O(n), Space Complexity: O(n).
    """
    if not root:
        return []

    result = []
    queue = deque([root])
    # Level 0 is left-to-right (False), Level 1 is right-to-left (True), and so on.
    reverse_order = False 

    # BFS traversal
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        # Apply zigzag ordering based on the level (reverse the list if needed)
        if reverse_order:
            current_level.reverse()
            
        result.append(current_level)
        
        # Alternate the direction for the next level
        reverse_order = not reverse_order

    return result

# --- Test Cases ---
# Example 1
input1 = [3, 9, 20, None, None, 15, 7]
root1 = build_tree_from_list(input1)
output1 = zigzagLevelOrder(root1)
print(f"Example 1: Input: {input1} | Output: {output1}")
# Expected: [[3], [20, 9], [15, 7]]

# Example 2
input2 = [1]
root2 = build_tree_from_list(input2)
output2 = zigzagLevelOrder(root2)
print(f"Example 2: Input: {input2} | Output: {output2}")
# Expected: [[1]]

# Example 3
input3 = []
root3 = build_tree_from_list(input3)
output3 = zigzagLevelOrder(root3)
print(f"Example 3: Input: {input3} | Output: {output3}")
# Expected: []