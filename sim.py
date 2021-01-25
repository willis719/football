import random
from plays import Plays



name = input("What's your name? ")
print(f"Hey {name} you are the new quarterback of this team.")
print("You have one final drive to win this game you are down 5 so we need a touchdown.")
print("You are running onto the field and get into the huddle...")



# Opening statement before each play
def start():
    start.counter += 1
    print(f"You come out the huddle and the defense is in {random.choice(Plays.defense_play)}")
    print("""What do you want to run:
    1. Deep pass
    2. Run left
    3. Run right
    4. Quick pass""")
    play = int(input("> "))

    if play == 1:
        Plays.play_one("pass")
    if play == 2:
        Plays.play_two("run left")
    if play == 3:
        Plays.play_three("run right")
    if play == 4:
        Plays.play_four("quick pass")

start.counter = 0
    



    
while sum(Plays.yards) <= 50:
    if sum(Plays.yards) >= 50 or Plays.yards_left <= 0:
        print("Touchdown! You won the game!")
        break
    elif start.counter == 4 and sum(Plays.yards) < 25:
        print("Turnover on downs. You lost the game")
        exit()
    else:
        start()