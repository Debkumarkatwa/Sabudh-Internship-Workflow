# Problem 6: Edit Distance

def minDistance(word1: str, word2: str) -> int:
    """
    Calculates the minimum edit distance using dynamic programming (Levenshtein distance).
    Time Complexity: O(m * n), Space Complexity: O(m * n).
    """
    m, n = len(word1), len(word2)
    # dp[i][j] stores the minimum operations to convert word1[:i] to word2[:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize the first row (converting word1[:0] to word2[:j] requires j insertions)
    for j in range(n + 1):
        dp[0][j] = j
        
    # Initialize the first column (converting word1[:i] to word2[:0] requires i deletions)
    for i in range(m + 1):
        dp[i][0] = i
        
    # Fill the DP table
    # Loop through all prefixes of word1 (i) and word2 (j)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # If characters match, cost is the same as the diagonal cell (no new operation)
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            # If characters don't match, take the minimum of three operations + 1 cost:
            # 1. dp[i-1][j] (Delete from word1)
            # 2. dp[i][j-1] (Insert into word1)
            # 3. dp[i-1][j-1] (Replace in word1)
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],      # Deletion
                                   dp[i][j - 1],      # Insertion
                                   dp[i - 1][j - 1])  # Replacement
                                   
    # The result is in the bottom-right cell
    return dp[m][n]

# --- Test Cases P6 ---
# Example 1
word1_1, word2_1 = "horse", "ros"
output1 = minDistance(word1_1, word2_1)
print(f"Example 1: Input: '{word1_1}', '{word2_1}' | Output: {output1}")
# Expected: 3

# Example 2
word1_2, word2_2 = "intention", "execution"
output2 = minDistance(word1_2, word2_2)
print(f"Example 2: Input: '{word1_2}', '{word2_2}' | Output: {output2}")
# Expected: 5