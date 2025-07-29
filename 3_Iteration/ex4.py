computer_number = 15

user_number = int(input("Enter a positive number: "))
counter = 1

while user_number != computer_number:
    if computer_number > user_number:
        print("Higher!")
    else:
        print("Lower!")
    user_number = int(input("Enter a positive number: "))
    counter += 1

print(f"You have guessed the number {computer_number} in {counter} turns.")