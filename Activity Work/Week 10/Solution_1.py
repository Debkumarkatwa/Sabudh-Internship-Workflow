from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth_recursive(root: Optional[TreeNode]) -> int:
    """Return the maximum depth (height) of the binary tree using recursion."""
    if root is None:
        return 0
    left_depth = maxDepth_recursive(root.left)
    right_depth = maxDepth_recursive(root.right)
    return 1 + max(left_depth, right_depth)

def maxDepth_iterative(root: Optional[TreeNode]) -> int:
    """Return the maximum depth using level-order traversal (BFS)."""
    if root is None:
        return 0
    q = deque([root])
    depth = 0
    while q:
        for _ in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        depth += 1
    return depth

# Example usage:
# Construct tree:    1
#                  /   \
#                 2     3
#                /
#               4
if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
    print("Max depth (recursive):", maxDepth_recursive(root))  # 3
    print("Max depth (iterative):", maxDepth_iterative(root))  # 3