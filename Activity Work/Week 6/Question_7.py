def countConsistentStrings(allowed, words):
    count = 0

    for word in words:
        if set(word).issubset(allowed):
            count += 1
            
    return count


allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]
print(countConsistentStrings(allowed, words)) 

allowed = "abc"
words = ["a","b","c","ab","ac","bc","abc"] 
print(countConsistentStrings(allowed, words))

allowed = "cad"
words = ["cc","acd","b","ba","bac","bad","ac","d"] 
print(countConsistentStrings(allowed, words))