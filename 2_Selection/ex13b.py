choice_computer = "scissors"

choice_player = input("What do you choose: paper, rock or scissors? ")

if choice_computer == choice_player:
    answer = "Tie!"
else:
    match choice_computer:
        case "paper":
            if choice_player == "rock":
                answer = "I win :-)"
            else:
                answer = "You win :-)"

        case "rock":
            if choice_player == "scissors":
                answer = "I win :-)"
            else:
                answer = "You win :-)"

        case "scissors":
            if choice_player == "paper":
                answer = "I win :-)"
            else:
                answer = "You win :-)"

print('You chose', choice_player)
print('I chose', choice_computer)
print(answer)