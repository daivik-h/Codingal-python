moves = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}

while True:

    user = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()


    if user == 'quit':

        break

    elif user in moves:

        print(f"Computer chooses {moves[user]}. You lose!")

    else:

        print("Invalid input. Try again.")