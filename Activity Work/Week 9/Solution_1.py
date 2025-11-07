# Problem 1: Longest Common Subsequence

def longestCommonSubsequence(text1: str, text2: str) -> int:
    """
    Finds the length of the longest common subsequence using dynamic programming.
    Time Complexity: O(m * n), Space Complexity: O(m * n).
    """
    m, n = len(text1), len(text2)
    # dp[i][j] stores the length of LCS of text1[:i] and text2[:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the DP table
    # Loop over all possible substrings
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # If the characters match, the LCS length increases by 1 
            # from the diagonal cell (LCS of shorter substrings).
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            # If characters don't match, take the maximum LCS from either
            # excluding the last character of text1 or text2.
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                
    # The result is in the bottom-right cell
    return dp[m][n]

# --- Test Cases ---
# Example 1
text1_1, text2_1 = "abcde", "ace"
output1 = longestCommonSubsequence(text1_1, text2_1)
print(f"Example 1: Input: '{text1_1}', '{text2_1}' | Output: {output1}")
# Expected: 3

# Example 2
text1_2, text2_2 = "abc", "abc"
output2 = longestCommonSubsequence(text1_2, text2_2)
print(f"Example 2: Input: '{text1_2}', '{text2_2}' | Output: {output2}")
# Expected: 3

# Example 3
text1_3, text2_3 = "abc", "def"
output3 = longestCommonSubsequence(text1_3, text2_3)
print(f"Example 3: Input: '{text1_3}', '{text2_3}' | Output: {output3}")
# Expected: 0