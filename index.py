
myList = ["a", "e", "i", "o", "u"]
count = 0
inputString = input("Enter a letter: ").lower()

for char in inputString:
    if char in myList:
        count += 1
print(f"The input string contains {count} vowels")
        