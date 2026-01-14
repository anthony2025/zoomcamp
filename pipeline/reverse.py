print("This line will be printed.")

# word is a string
def reverse_word(word):
    reversed = ""
    for letter in word:
            reversed = letter + reversed
    return reversed

# word is a string
def is_palindrome(word):
        return word == reverse_word(word)

# arr is an array of words
def check_all_palindromes(arr):
        for word in arr:
            if not is_palindrome(word):
                        return False
        return True

print("[heh, asa]", check_all_palindromes(["heh", "asa"]))
print("[hagh, as]", check_all_palindromes(["hagh", "as"]))

