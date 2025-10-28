import time
import random
#Variable Assignment
Player=Computer=Computer_Batting_Bowling=Player_Batting_Bowling=0
Choices=[1,2,3,4,5,6]
win_responses = [
    "Boom! That's a clean hit!",
    "Crushed it like a Rock:🪨!",
    "Victory is mine!",
    "One point for me — keep up!",
    "Too easy 😏",
    "Another W in the bag!",
    "Outplayed and outsmarted 🎯",
    "That’s how legends roll!",
    "You never saw that coming 😎",
    "And the crowd goes wild! 📣",
    "Skill issue, maybe? 😉",
    "Another flawless strike.",
    "Stacking up my victories 📈"
]
lose_responses = [
    "Oof... you got me!",
    "Rocked out of existence.",
    "That one stung...",
    "Alright, alright... you win this one.",
    "Let me come back stronger 🔥",
    "Okay, lucky shot 😅",
    "Guess I walked right into that one... 🤦",
    "Touché, you got me there.",
    "I’ll get you next time 💪",
    "Defeat accepted... for now.",
    "Even champions stumble sometimes 👀",
    "Consider this your lucky round 🍀",
    "Yikes... that didn’t go as planned."
]
draw_responses = [
    "Great minds think alike!",
    "Draw! Try again!",
    "We’re synced up today.",
    "Stalemate — go again!",
    "No points, no glory.",
    "Copycat 😜",
    "Well well... that was close!",
    "Locked in a perfect tie!",
    "Neither of us is backing down 💥",
    "Balance has been restored ⚖️",
    "It’s like we’re reading each other’s minds 🧠",
    "Too close to call — rematch!",
    "Twin moves, huh? 😏",
    "Looks like destiny wants a replay."
]
#Function Definition
def Display_Score():
    global Player
    global Computer
    print("The Score is",Player,":",Computer)
def Display_Winner():
    global Player
    global Computer
    if Player > Computer:
        # Player has higher score
        print(random.choice(win_responses))
        time.sleep(0.3)
        print("You are the winner🏆")
    elif Computer > Player:
        # Computer has higher score
        print(random.choice(lose_responses))
        time.sleep(0.3)
        print("Computer is the winner💀")
    else:
        print(random.choice(draw_responses))
        time.sleep(0.3)
        print("It's a draw⚖️")
    print("Exiting the Game........👋")
    time.sleep(10)
def Player_Batting():
    global Player
    global Computer
    global Choices
    while True:
        Computer_Choice = random.choice(Choices)
        Player_Choice_raw = input("Enter a Choice between 1 and 6: \n")
        try:
            Player_Choice = int(Player_Choice_raw)
        except ValueError:
            Exit = input("You've entered an invalid Choice, Wanna exit? Yes/No:\n").lower()
            if Exit == "yes":
                time.sleep(0.3)
                Display_Score()
                time.sleep(0.3)
                print("OK Exiting.....")
                time.sleep(1)
                break
            else:
                print("Continuing")
                time.sleep(0.3)
                continue

        if Player_Choice in Choices:
            print("I choose:", Computer_Choice)
            time.sleep(0.3)
            if Computer_Choice == Player_Choice:
                # wicket / out
                print(random.choice(lose_responses))
                time.sleep(0.3)
                Display_Score()
                time.sleep(0.3)
                break
            else:
                # player scores
                Player += Player_Choice
                time.sleep(0.3)
                print(random.choice(win_responses))
                time.sleep(0.3)
                Display_Score()
        else:
            Exit = input("You've entered an invalid Choice, Wanna exit? Yes/No:\n").lower()
            if Exit == "yes":
                time.sleep(0.3)
                Display_Score()
                time.sleep(0.3)
                print("OK Exiting.....")
                time.sleep(1)
                break
            else:
                print("Continuing")
                time.sleep(0.3)
def Computer_Batting():
    global Player
    global Computer
    global Choices
    while True:
        Computer_Choice = random.choice(Choices)
        Player_Choice_raw = input("Enter a Choice between 1 and 6:\n")
        try:
            Player_Choice = int(Player_Choice_raw)
        except ValueError:
            Exit = input("You've entered an invalid Choice, Wanna exit? Yes/No:\n").lower()
            if Exit == "yes":
                time.sleep(0.3)
                Display_Score()
                time.sleep(0.3)
                print("OK Exiting.....")
                time.sleep(1)
                break
            else:
                print("Continuing")
                time.sleep(0.3)
                continue

        if Player_Choice in Choices:
            print("I choose:", Computer_Choice)
            time.sleep(0.3)
            if Computer_Choice == Player_Choice:
                # wicket / out
                print(random.choice(lose_responses))
                time.sleep(0.3)
                Display_Score()
                time.sleep(0.3)
                break
            else:
                # computer scores
                Computer += Computer_Choice
                time.sleep(0.3)
                print(random.choice(win_responses))
                time.sleep(0.3)
                Display_Score()
        else:
            Exit = input("You've entered an invalid Choice, Wanna exit? Yes/No:\n").lower()
            if Exit == "yes":
                time.sleep(0.3)
                Display_Score()
                time.sleep(0.3)
                print("OK Exiting.....")
                time.sleep(1)
                break
            else:
                print("Continuing")
                time.sleep(0.3)
def Determine_Odd_Even():
    global Computer_Odd_Even
    global Player_Odd_Even
    Odd_Even_Sum=(Player_Odd_Even+Computer_Odd_Even)
    if (Odd_Even_Sum)%(2)!=(0):
        return("odd")
    elif (Odd_Even_Sum)%(2)==(0):
        return("even")
#Main Execution Part
print("Loading the game...")
time.sleep(1)
print("🙏Welcome🙏")
time.sleep(0.3)
print("To The One And Only....")
time.sleep(0.3)
print("Ayushman Verma's")
time.sleep(0.3)
print("Python 🐍 based Hand 🖐️ Cricket 🏏 Game 🎮")
time.sleep(0.3)
print("Note\n*In this game:\nThe Score is Given as Player:Computer")
Odd_Even=input("Choose Odd or Even:\n").lower()
Player_Odd_Even=int(input("Enter the number:\n"))
Computer_Odd_Even=random.choice(Choices)
print("I chose:",Computer_Odd_Even)
time.sleep(0.3)
if Odd_Even in ["odd", "even"] and Player_Odd_Even in Choices:
    if (Odd_Even==Determine_Odd_Even()):
        print("The Outcome is:",Determine_Odd_Even())
        time.sleep(0.3)
        print("You won the toss")
        time.sleep(0.3)
        print("Choose Batting or Bowling:")
        time.sleep(0.3)
        Player_Batting_Bowling=int(input("Batting:1 or Bowling:2\n"))
        time.sleep(0.3)
        if Player_Batting_Bowling==1:
            print("You chose Batting")
            Player_Batting()
            print("It's my turn for batting now ")
            time.sleep(0.3)
            Computer_Batting()
            time.sleep(0.3)
            Display_Winner()
        else:
            print("You chose Bowling")
            Computer_Batting()
            print("It's your turn for batting now ")
            time.sleep(0.3)
            Player_Batting()
            time.sleep(0.3)
            Display_Winner()
    else:
        print("The Outcome is:",Determine_Odd_Even())
        time.sleep(0.3)
        print("I won the toss")
        Computer_Batting_Bowling=(random.choice([1,2]))
        time.sleep(0.3)
        if Computer_Batting_Bowling==1:
            print("I chose Batting")
            Computer_Batting()
            print("It's your turn for batting now ")
            time.sleep(0.3)
            Player_Batting()
            time.sleep(0.3)
            Display_Winner()
        else:
            print("I chose Bowling")
            Player_Batting()
            print("It's my turn for batting now ")
            time.sleep(0.3)
            Computer_Batting()
            time.sleep(0.3)
            Display_Winner()
else:
    print("Invalid Input, Exiting the game")
    time.sleep(0.3)
    Display_Score()
    time.sleep(0.3)
    print("Exiting.....")
    time.sleep(1)