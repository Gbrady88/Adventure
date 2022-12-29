# Enhanced Adventure Game
# Gerald Brady
# 12/17/2020

def intro():
    # Get the user's favorite restaurant.
    user_restaurant = input("What is your favorite restaurant?")
    # Get the user's best friend.
    user_bestFriend = input("Who is your best friend?")
    # Get the user's favorite drink.
    user_drink = input("What is your favorite drink?")
    # Get the user's favorite food.
    user_food = input("What is your favorite food?")

    # directory of the user's info
    user_info = {
        "restaurant": user_restaurant,
        "bestFriend": user_bestFriend,
        "drink": user_drink,
        "food": user_food
    }

    # Print user personalized adventure intro.
    print("It’s a beautiful day outside. You see that it's a clear weather forecast, "
          "so you decide to go to a happy hour at " + user_info["restaurant"] + " with your best friend "
          + user_info["bestFriend"] + ". You and " + user_info["bestFriend"] + " love " + user_info["drink"] + "'s and "
          + user_info["food"] + "'s, which " + user_info["restaurant"] + " are known for. " + user_info["bestFriend"]
          + " is going to meet you there. You have the option to drive or take public transportation."
            " Which do you choose?")


def adventure():
    # opens story
    f = open("story.txt", "r")
    # File becomes recognized as lines that can be referenced.
    line = f.readlines()

    # Question 1
    driveOrSub = input("drive or subway?")
    # list for drive or subway
    ds = ["drive", "subway"]

    # if user input equals the first element in the list
    if driveOrSub == ds[0]:
        print(line[1])
        # Question 2
        stopOrGo = input("stop or go?")
        sg = ["stop", "go"]

        # if user input equals the second element in the list
        if stopOrGo == sg[0]:
            print(line[3])
            # Question 3
            returnOrCut = input("return or cut?")
            rc = ["return", "cut"]

            if returnOrCut == rc[0]:
                print(line[5])

            elif returnOrCut == rc[1]:
                print(line[7])
            else:
                print(line[29])

        elif stopOrGo == sg[1]:
            print(line[9])
            # Question 3
            buyOrNot = input("buy or not?")
            bn = ["buy", "not"]

            if buyOrNot == bn[0]:
                print(line[11])
            elif buyOrNot == bn[1]:
                print(line[13])
            else:
                print(line[29])

        else:
            print(line[29])

    elif driveOrSub == ds[1]:
        print(line[15])

        # Question 2b
        yesOrNo = input("Do you you give him money, yes or no?")
        yn = ["yes", "no"]

        if yesOrNo == yn[0]:
            print(line[17])

            # Question 3
            lyftOrTrain = input("lyft or train?")
            lt = ["lyft", "train"]

            if lyftOrTrain == lt[0]:
                print(line[19])

            elif lyftOrTrain == lt[1]:
                print(line[21])
            else:
                print(line[29])

        elif yesOrNo == yn[1]:
            print(line[23])
        barOrTable = input("bar or table?")
        bt = ["bar", "table"]

        if barOrTable == bt[0]:
            print(line[25])

        elif barOrTable == bt[1]:
            print(line[27])

        else:
            print(line[29])

    else:
        print(line[29])
    # closes the story file
    f.close()

def title(name):
    print()
    print("**** " + name + "'s Adventure ****")
    print()

def main():
    user_name = input("What is your name?")
    title(user_name)
    intro()
    adventure()


# to start program
main()
