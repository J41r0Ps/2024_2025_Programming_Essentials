number = int(input("Enter a number, stop by entering a zero: "))
product = 1
i = 0

while number != 0:
    product *= number
    number = int(input("Enter a number, stop by entering a zero: "))
    i += 1
print(f"The product of the {i} numbers is {product}")