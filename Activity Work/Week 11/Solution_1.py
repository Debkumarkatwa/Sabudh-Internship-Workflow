# Problem 1: Clone Graph

class Node:
    """Definition for a graph node."""
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# Helper functions for input simulation and output verification
def build_graph_from_adjList(adjList):
    """
    Builds a graph from an adjacency list (where index i represents node val i+1).
    Returns the node with val=1 (first node).
    """
    if not adjList:
        return None
        
    # 1. Create all nodes
    nodes = {i + 1: Node(i + 1) for i in range(len(adjList))}
    
    # 2. Assign neighbors
    for i, neighbors_val in enumerate(adjList):
        node_val = i + 1
        node = nodes[node_val]
        for neighbor_val in neighbors_val:
            if neighbor_val in nodes:
                node.neighbors.append(nodes[neighbor_val])
                
    return nodes.get(1)

def graph_to_adjList(node1: Node):
    """
    Converts a cloned graph back to an adjacency list for verification.
    Assumes node values are 1-indexed.
    """
    if not node1:
        return []
        
    # Use BFS to find all nodes and map their structure
    adjList_map = {}
    visited = set()
    queue = [node1]
    
    while queue:
        node = queue.pop(0)
        if node.val in visited:
            continue
        visited.add(node.val)
        
        # Initialize the adjacency list for the current node
        adjList_map[node.val] = []
        
        # Add neighbors' values to the list and queue unvisited neighbors
        for neighbor in node.neighbors:
            adjList_map[node.val].append(neighbor.val)
            if neighbor.val not in visited:
                queue.append(neighbor)
    
    # Sort the neighbor lists and convert the map back to the required list format
    # The output list must be indexed 0 to N-1, corresponding to node val 1 to N.
    max_val = max(adjList_map.keys()) if adjList_map else 0
    result = [[] for _ in range(max_val)]
    
    for val, neighbors in adjList_map.items():
        neighbors.sort()
        if 1 <= val <= max_val:
            result[val - 1] = neighbors
            
    return result

def cloneGraph(node: Node) -> Node:
    """
    Returns a deep copy (clone) of the connected undirected graph using DFS.
    Time Complexity: O(V + E), Space Complexity: O(V).
    """
    if not node:
        return None
        
    # Map to store copies: {original_node.val: cloned_node}
    # This prevents infinite loops (by tracking visited nodes) and allows neighbor linkage.
    cloned_map = {}

    def dfs(original_node):
        # If the node has already been copied, return the copy
        if original_node.val in cloned_map:
            return cloned_map[original_node.val]
            
        # 1. Create the copy
        new_node = Node(original_node.val)
        
        # 2. Map the copy immediately to mark it as visited and avoid cycles
        cloned_map[original_node.val] = new_node
        
        # 3. Recursively clone and link neighbors
        for neighbor in original_node.neighbors:
            new_node.neighbors.append(dfs(neighbor))
            
        return new_node
        
    # Start DFS from the given node (node with val=1)
    return dfs(node)

# --- Test Cases ---
# Example 1
adjList1 = [[2, 4], [1, 3], [2, 4], [1, 3]]
graph1 = build_graph_from_adjList(adjList1)
cloned_node1 = cloneGraph(graph1)
output1 = graph_to_adjList(cloned_node1)
print(f"Example 1: Input: {adjList1} | Output: {output1}")
# Expected: [[2, 4], [1, 3], [2, 4], [1, 3]]

# Example 2
adjList2 = [[]]
graph2 = build_graph_from_adjList(adjList2)
cloned_node2 = cloneGraph(graph2)
output2 = graph_to_adjList(cloned_node2)
print(f"Example 2: Input: {adjList2} | Output: {output2}")
# Expected: [[]]

# Example 3
adjList3 = []
graph3 = build_graph_from_adjList(adjList3)
cloned_node3 = cloneGraph(graph3)
output3 = graph_to_adjList(cloned_node3)
print(f"Example 3: Input: {adjList3} | Output: {output3}")
# Expected: []