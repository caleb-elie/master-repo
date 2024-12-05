def is_palindrome(phrase):
    cleaned_phrase = ''.join(char.lower() for char in phrase if char.isalnum())
    
    if cleaned_phrase == cleaned_phrase[::-1]:
        print(f"'{phrase}' is a palindrome")
    else:
        print(f"'{phrase}' is not a palindrome")

word = input("Enter a phrase or word: ")
is_palindrome(word)
