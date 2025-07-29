child_age = int(input("How old are you: "))
father_age = int(input("How old is your father: "))

if father_age < child_age * 2:
    print("The situation is no longer possible for your ages")
else:
    counter = 0
    while child_age * 2 != father_age:
        child_age += 1
        father_age += 1
        counter += 1
    print(f"Within {counter} your father will have twice your age")
    print(f"Your father will be {father_age} and you will be {child_age}")