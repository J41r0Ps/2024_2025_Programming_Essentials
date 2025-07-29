final_digit = int(input("What final digit do you want to check the number on: "))
counter = 0

for i in range(10):
    number = int(input("Enter a number: "))
    if number % 10 == final_digit:
        counter += 1
print(counter,"out of 10 numbers end on",7)