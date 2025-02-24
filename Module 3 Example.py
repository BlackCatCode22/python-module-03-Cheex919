numbers = []

while True:
    user_input = input("Enter a number or 'done' to finish: ")

    if user_input == 'done':
        print("Try captializing 'done' ")

    if user_input == 'Done':
        break

    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter an integer or type 'done' ")


if numbers:
    print("Maximum number in the sequence:", max(numbers))
    print ("Minimum number in the sequence:", min(numbers))
    print ("Thanks for using me!")
else:
    print("No numbers were entered. Enter a number again")