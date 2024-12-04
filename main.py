user = input("Enter a number: ")
total = 0

if not user.isdigit():
    print("Please enter a valid number.")
else:
    try:
        for digit in user:
            total += int(digit)
        print("The sum of digits is ", total)
    except Exception as e:
        print("An error occurred")
    