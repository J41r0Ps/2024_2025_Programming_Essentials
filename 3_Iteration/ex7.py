initial_limit = int(input("Initial limit: "))
final_limit = int(input("Final limit: "))

if initial_limit > final_limit:
    print("The initial limit must be smaller than the final limit!")
else:
    print(f"Sum of numbers from {initial_limit} till {final_limit}")
    sum = initial_limit

    if initial_limit == final_limit:
        print(sum)
    else:
        for i in range (initial_limit,final_limit):
            sum += i + 1
            print(f"+ {i + 1} --> {sum}")