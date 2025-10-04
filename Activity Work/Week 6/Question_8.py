def removeDuplicates(str):
    stack = []
    for char in str:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
            
    return ''.join(stack)

# Example usage:
print(removeDuplicates("abbaca"))  # Output: "ca"
print(removeDuplicates("azxxzy"))  # Output: "ay"