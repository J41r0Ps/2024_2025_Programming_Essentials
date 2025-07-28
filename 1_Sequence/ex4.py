first_name = input("Enter the first name: ")
second_name = input("Enter the second name: ")

print("Before changing: " + first_name + " " + second_name)

temp = second_name
second_name = first_name
first_name = temp

print("After changing: " + first_name + " " + second_name)