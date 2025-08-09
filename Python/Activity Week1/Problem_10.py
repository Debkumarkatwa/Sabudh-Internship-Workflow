'''
Define a function which counts vowels and consonants in a word. 
● Test case 1: 
    Input : pythonlobby 
    Output :   
      vowel : 2  
      Consonants: 9 
● Test case 2: 
    Input : sabudhfoundation 
    Output :  
      vowel : 7 
      Constants: 9 
'''
def count_vowels_and_consonants(word):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0

    for char in word:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count


word = input("Enter a word: ")
vowel_count, consonant_count = count_vowels_and_consonants(word)
print(f"Vowel : {vowel_count}")
print(f"Consonant : {consonant_count}")