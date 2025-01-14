import sys
import random

def main():
    victory = False
    Wins = [0, 0]
    while not victory:
        if Wins[0] == 2:
            print("You win")
            victory = True
            break
        elif Wins[1] == 2:
            print("You lost to random numbers :(")
            victory = True
            break

        Actions =("Rock","Paper","Scissors")
        
        ActionLen = len(Actions)
        choice = 0
        AiChoice = 0
        for i,Action in enumerate(Actions, start = 1):
            print(f"{i}.  {Action}")

        choice = int(input("Choose rock, paper or scissors: "))
        if choice in range(ActionLen + 1):
            print(f"You choose {Actions[choice - 1]}")

        else:
            print("choice not valid")
            sys.exit(1)
        AiChoice = AiAction(Actions)
        PlChoice = Actions[choice - 1]
        print(f"The computer choose {AiChoice}")
        VictoryCheck(PlChoice,AiChoice,Actions,Wins)

def AiAction(Actions):
    n = random.randrange(1,4)
    Select = Actions[n - 1]
    return Select

def VictoryCheck(PlChoice,AiChoice,Actions,Wins):
    PL = Actions.index(PlChoice)
    AI = Actions.index(AiChoice)
    if PL == AI:
        print("Draw")
        return
    elif (PL == 1 and AI == 2) or (PL == 2 and AI == 3) or (PL == 3 and AI == 1):
        print(f"{AiChoice} wins")
        Wins[1] += 1
        return
    else:
        print(f"{PlChoice} wins")
        Wins[0] += 1
        return


main()