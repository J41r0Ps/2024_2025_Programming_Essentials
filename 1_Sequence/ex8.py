current_hour = int(input("Enter the current hour: "))
time_to_wait = int(input("How long do you want to wait: "))

print(f"The alarm will sound at {(current_hour + time_to_wait) % 24}h.")