# 1. Fibonacci generator
def fibonacci(n):
    a, b = 0, 1     # Initialize first two Fibonacci numbers
    for _ in range(n):
        yield a
        a, b = b, a + b

print("First 10 Fibonacci numbers:")    # Testing the fibonacci generator
print(list(fibonacci(10)))


# 2. Prime number generator
def is_prime(num):  # fubction to check if a number is prime
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def primes_up_to(n):    # generator for prime numbers up to n
    for num in range(2, n + 1):
        if is_prime(num):   # check if num is prime
            yield num

print("\nPrime numbers up to 100:") # Testing the primes_up_to generator
print(list(primes_up_to(100)))


# 3. String-to-words generator
def words_from_string(s):
    for word in s.split():
        yield word

print("\nWords in string:") # Testing the words_from_string generator
for word in words_from_string("The quick brown fox jumps over the lazy dog."):
    print(word)


# 4. Unique words generator
def unique_words(word_list):
    seen = set()
    for word in word_list:  # iterate through each word
        w = word.lower()
        if w not in seen:   # check if word is already seen
            seen.add(w)
            yield word

print("\nUnique words from list:")  # Testing the unique_words generator
print(list(unique_words(["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"])))


# 5. Sublists generator of length n
def sublists(lst, n):
    for i in range(len(lst) - n + 1):   # iterate through list
        yield lst[i:i+n]

print("\nSublists of length 3:")    # Testing the sublists generator
print(list(sublists([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)))
