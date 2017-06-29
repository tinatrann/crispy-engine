gameOn = True

while gameOn:
    print("A zombie apocalypse has started in Massachusetts. You're currently living in California.")
    print("What will be your first reaction.")
    print("Months later the zombies reach the west coast. You have only two options.")
    print("1. Let the zombies come and take you.")
    print("2. Start running to the nearest grocery store because there is food and water.")
    option = int(input("What would you do next? Type '1' to choose one or '2' to choose two. "))
    if option == 1:
        print("You're done with life and lost the will to keep living. You see zombies walking towards you.")
        print("You tell the zombies, 'Come and take me.'")
        print("Once bitten by a zombie the Solanum virus enters your body.")
        print("It spreads throughout your body and moves towards your brain.")
        print("Your brain mutates into an organ that does not require oxygen.")
        print("You're now a zombie.")
        print("Do you want to play again?")
        user_input = input("Type yes or no. ")
        if user_input == "no":
            gameOn = False
        if user_input == "yes":
            gameOn = True

    if option == 2:
        print("You peek out of the window to make sure there are no zombies around.")
        print("Once you see that there are no zombies on the street, you open the door and run to the nearest grocery store.")
        print("When you turn around the corner, you run into a zombie.")
        print("You try to run away as fast as you can but you are not fast enough.")
        print("The zombie catches you.")
        print("Once bitten by a zombie the Solanum virus enters your body.")
        print("It spreads throughout your body and moves towards your brain.")
        print("Your brain mutates into an organ that does not require oxygen.")
        print("You're now a zombie.")
        print("Do you want to play again?")
        user_input = input("Type yes or no.")
        if user_input == "no":
            gameOn = False
        if user_input == "yes":
            gameOn = True

print("Game over.")
