# Problem 4: Check if each internal node of a BST has exactly one child

def hasOnlyOneChild(preorder: list[int]) -> str:
    """
    Checks if every non-leaf node in the BST defined by 'preorder' has exactly one child.
    Time Complexity: O(n), Space Complexity: O(1).
    
    Approach: In a single-child BST chain, all nodes following a parent 
    must be on the same side (either all greater or all smaller) until 
    the chain ends or reverses. The next two elements in the preorder 
    traversal relative to the current root (next_val and next_next_val) 
    must not straddle the root's value.
    """
    n = len(preorder)
    
    # Only internal nodes (non-leaf nodes) are checked. 
    # The last element is always a leaf, so we only need to check up to n-2.
    for i in range(n - 2):
        root_val = preorder[i]
        next_val = preorder[i + 1]
        next_next_val = preorder[i + 2]
        
        # Check if root_val is between next_val and next_next_val (i.e., straddling condition)
        # If root_val is between them, it means next_val and next_next_val 
        # would form left and right children of root_val, violating the one-child rule.
        
        # Case 1: next_val < root_val and next_next_val > root_val
        condition1 = (next_val < root_val) and (next_next_val > root_val)
        
        # Case 2: next_val > root_val and next_next_val < root_val
        condition2 = (next_val > root_val) and (next_next_val < root_val)
        
        if condition1 or condition2:
            return "No"
            
    return "Yes"

# --- Test Cases ---
# Test case 1
preorder1 = [20, 10, 11, 13, 12]
output1 = hasOnlyOneChild(preorder1)
print(f"Test case 1: Input: {preorder1} | Output: {output1}")
# Expected: Yes

# Test case 2
preorder2 = [15, 30, 25, 18, 20]
output2 = hasOnlyOneChild(preorder2)
print(f"Test case 2: Input: {preorder2} | Output: {output2}")
# Expected: Yes