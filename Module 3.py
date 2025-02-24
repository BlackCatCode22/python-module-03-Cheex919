def main():
    total = 0
    count = 0

# Input numbers / Done prompt
    while True:
        user_input = input("Enter a Number (or 'Done' to finish): ")

        if user_input.lower() == 'done':
            break

        try:
        #Program to show numbers.
            number = int(user_input)
            total += number
            count += 1
        except ValueError:
            print("Invalid input. Please enter a Number.")

    if count > 0:
        average = total / count
        print(f"Total: {total}, Count: {count}, Average: {average:.2f}")
    else:
        print("No valid numbers were entered.")


if __name__ == "__main__":
    main()