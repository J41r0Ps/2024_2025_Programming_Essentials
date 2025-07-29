number = int(input("Enter a number: "))
zeros = sixes = 0

while number != 0:
    digit = number % 10
    if digit == 6:
        sixes += 1
    if digit == 0:
        zeros += 1
    number //= 10

print(f"The number consists of {zeros} and {sixes} sixes")