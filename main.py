import random
import time


auth = 0          # Authentication
rounds = 0        # Amount of rounds
turn = 0          # Boolean value:  0 for Player 1 and 1 for Player 2
p1score = 0
p2score = 0

while auth == 0:
    code = input("Enter the auth code: ")
    if code.upper() == "BOOLEAN":
        print("Correct auth code has been entered")
        p1 = str(input("What would Player 1 like to name themselves?: "))
        p2 = str(input("What would Player 2 like to name themselves?: "))
        print(p1, "and", p2, "the game shall now commence!")
        auth = 1
        time.sleep(3)

    if auth == 1:
        while rounds < 5:           # To make sure that there are only 5 rounds played
            while turn == 0:
                p1roll = input("Press Y and confirm with Enter to roll dice, " + str(p1) + ": ")
                if p1roll.upper() == "Y":
                    p1dice1 = random.randint(1, 6)
                    p1dice2 = random.randint(1, 6)
                    p1dice3 = random.randint(1, 6)
                    print("Rolling 1st Dice...")
                    time.sleep(1)
                    print("You rolled a", str(p1dice1) + "!")
                    time.sleep(0.5)
                    print("Rolling 2nd Dice...")
                    time.sleep(1)
                    print("You rolled a", str(p1dice2) + "!")
                    p1total = p1dice1 + p1dice2
                    turn = 1

                    if p1dice1 == p1dice2:
                        print("You rolled a double! You can roll another dice!")
                        time.sleep(0.5)
                        print("Rolling 3rd Dice...")
                        print("You rolled a", str(p1dice3) + "!")
                        p1total = p1dice3 + p1total
                    else:
                        p1total = p1total

                    if p1total % 2 == 0:          #To check if it is even or odd
                        p1score = p1score + p1total + 10
                        print("As your score is even, you will receive an additional 10 points! Current score:", str(p1score))
                    elif p1total % 2 == 1: #To check if it is
                        p1score = p1score + p1total - 5

                        if p1score == 0 or p1score > 0:
                            print("As your score is odd, 5 points will be subtracted from your total. Current score:", str(p1score))
                        else:
                            p1sc = 0
                            print("As your score was odd, 5 points were subtracted, however, the total went below 0, but as per the game rules, the score cannot go below 0. Current score: 0")

            while turn == 1:
                p2roll = input("Press Y and confirm with Enter to roll dice, " + str(p2) + ": ")
                if p2roll.upper() == "Y":
                    p2dice1 = random.randint(1, 6)
                    p2dice2 = random.randint(1, 6)
                    p2dice3 = random.randint(1, 6)
                    print("Rolling 1st Dice...")
                    time.sleep(1)
                    print("You rolled a", str(p2dice1) + "!")
                    time.sleep(0.5)
                    print("Rolling 2nd Dice...")
                    time.sleep(1)
                    print("You rolled a", str(p2dice2) + "!")
                    p2total = p2dice1 + p2dice2
                    turn = 0
                    rounds = rounds + 1

                    if p2dice1 == p2dice2:
                        print("You rolled a double! You can roll another dice!")
                        time.sleep(0.5)
                        print("Rolling 3rd Dice...")
                        print("You rolled a", str(p2dice3) + "!")
                        p2total = p2dice3 + p2total
                    else:
                        p2total = p2total

                    if p2total % 2 == 0:          #To check if it is even or odd
                        p2score = p2score + p2total + 10
                        print("As your score is even, you will receive an additional 10 points! Current score:", str(p2score))
                    elif p2total % 2 == 1: #To check if it is
                        p2score = p2score + p2total - 5

                        if p2score == 0 or p2score > 0:
                            print("As your score is odd, 5 points will be subtracted from your total. Current score:", str(p2score))
                        else:
                            p2score = 0
                            print("As your score was odd, 5 points were subtracted, however, the total went below 0, but as per the game rules, the score cannot go below 0. Current score: 0")

            while rounds == 5:
                while p1score == p2score:
                    print("\n As both of your scores are the same, you will have to continue to the tiebraker round, where each of you will have to roll 1 dice until someone emerges victorious!\n")
                    time.sleep(1)
                    p1roll = input("Press Y and confirm with Enter to roll dice, " + str(p1) + ": ")
                    if p1roll.upper() == "Y":
                        p1dice1 = random.randint(1, 6)
                        print("Rolling the Dice...")
                        time.sleep(1)
                        print("You rolled a", str(p1dice1) + "!")
                        p1total = p1dice1

                        if p1total % 2 == 0:
                            p1score = p1score + p1total + 10
                        elif p1total % 2 == 1:
                            p1score = p1score + p1total - 5
                        
                            if p1score == 0 or p1score > 0:
                                print("As your score is odd, 5 points will be subtracted from your total! Current score:", str(p1score))
                            elif p1score < 0:
                                p1score = 0
                                print("As your score was odd, 5 points were subtracted, however, the total went below 0, but as per the game rules, the score cannot go below 0. Current score: 0")

                    time.sleep(0.75)
                    p2roll = input("Press Y and confirm with Enter to roll dice, " + str(p2) + ": ")
                    if p2roll.upper() == "Y":
                        p2dice1 = random.randint(1, 6)
                        print("Rolling the Dice...")
                        time.sleep(1)
                        print("You rolled a", str(p2dice1) + "!")
                        p2total = p2dice1

                        if p1total % 2 == 0:
                            p1score = p1score + p1total + 10
                        elif p1total % 2 == 1:
                            p1score = p1score + p1total - 5
                        
                            if p1score == 0 or p1score > 0:
                                print("As your score is odd, 5 points will be subtracted from your total! Current score:", str(p1score))
                            elif p1score < 0:
                                p1score = 0
                                print("As your score was odd, 5 points were subtracted, however, the total went below 0, but as per the game rules, the score cannot go below 0. Current score: 0")

                if p1score > p2score:
                    time.sleep(1)
                    print("The scores have been finalised, and...")
                    time.sleep(1.5)
                    print("The winner is", p1, "with", p1score, "points!")
                    rounds = 69
                else:
                    time.sleep(1)
                    print("The scores have been finalised, and...")
                    time.sleep(1.5)
                    print("The winner is", p2, "with", p2score, "points!")
                    rounds = 69

        scores = open("scores.txt", "w")
        scores.write(p1 + " - " + p1score + "\n" + p2 + " - " + p2score)
        scores.close()
