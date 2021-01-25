import random




class Plays():
    


    # List for yards for each play
    
    deep_yard = ["Touchdown", 0, "Interception", 10, 10, 15, 15, 20, 20]
    run_yard = [-2, 0, 0, 5, 5, 5, 7, 7, 10, 10, "touchdown"]
    quick_yard = [0, 3, 5, 5, 5, 7, 7, 7, 7, 7, 10, "touchdown"]
    downs = ["first", "second", "third", "fourth"]

    # Different defensive plays. I want to add more
    defense_play = ["blitz", "cover 1", "cover 2"]

    #want to store yards from each play in here
    yards = [0]

    yards_left = 50

    def_play = random.choice(defense_play)    

    #Deep pass play
    def play_one(self):
        
    # Gives random yards for a deep pass
        play_result = random.choice(Plays.deep_yard)

    # Defensive play that is a weakness to the deep pass
        if Plays.def_play == Plays.defense_play[0]:
            play_result = Plays.deep_yard[1]
            Plays.yards.append(Plays.deep_yard[1])


        print("You are running a deep pass")

        if play_result == Plays.deep_yard[0]:
            print("You threw a Touchdown!!! You are the hero of the town!")
            exit()

        elif play_result == Plays.deep_yard[1]:
            print("You threw an incomplete pass.")
            Plays.yards.append(Plays.deep_yard[1])


        elif play_result == Plays.deep_yard[2]:
            print("You threw an interception and lost the game. Boo you suck!")
            exit()

        elif play_result == Plays.deep_yard[3] or play_result == Plays.deep_yard[4]:
            print("Nice throw for a 10 yard completion.")
            Plays.yards.append(Plays.deep_yard[3])


        elif play_result == Plays.deep_yard[5] or play_result == Plays.deep_yard[6]:
            print("Great throw for a 15 yard completion.")
            Plays.yards.append(Plays.deep_yard[5])


        elif play_result == Plays.deep_yard[7] or play_result == Plays.deep_yard[8]:
            print("Wow amazing completion for 20 yards.")
            Plays.yards.append(Plays.deep_yard[7])

        global yards_left
        Plays.yards_left = Plays.yards_left - Plays.yards[-1]
        print(f"You have {Plays.yards_left} yards to go.")


    # Run left play
    def play_two(self):

    # Random run yardage displayed
        play_result = random.choice(Plays.run_yard)

        if Plays.def_play == Plays.defense_play[0]:
            play_result = Plays.run_yard[0]
            Plays.yards.append(Plays.run_yard[0])


        print("You are running the ball to the left.")

        if play_result == Plays.run_yard[0]:
            print("Bad play call! You lost 2 yards.")
            Plays.yards.append(Plays.run_yard[0])

        elif play_result == Plays.run_yard[1] or play_result == Plays.run_yard[2]:
            print("You didnt gain any yards.")
            Plays.yards.append(Plays.run_yard[1])

        elif play_result == Plays.run_yard[3] or play_result == Plays.run_yard[4] or play_result == Plays.run_yard[5]:
            print("Solid run! You gained 5 yards.")
            Plays.yards.append(Plays.run_yard[3])

        elif play_result == Plays.run_yard[6] or play_result == Plays.run_yard[7]:
            print("Good blocking! You gained 7 yards.")
            Plays.yards.append(Plays.run_yard[6])

        elif play_result == Plays.run_yard[8] or play_result == Plays.run_yard[9]:
            print("Fantastic execution! You gained 10 yards.")
            Plays.yards.append(Plays.run_yard[8])

        elif play_result == Plays.run_yard[10]:
            print("Amazing run for a touchdown!!! You won the game!!!")
            exit()

        global yards_left
        Plays.yards_left -= Plays.yards[-1]
        print(f"You have {Plays.yards_left} yards to go.")





    def play_three(self):

        play_result = random.choice(Plays.run_yard)

        if Plays.def_play == Plays.defense_play[0]:
            play_result = Plays.run_yard[0]
            Plays.yards.append(Plays.run_yard[0])

        print("You are running the ball to the right.")

        if play_result == Plays.run_yard[0]:
            print("Bad play call! You lost 2 yards.")
            Plays.yards.append(Plays.run_yard[0])

        elif play_result == Plays.run_yard[1] or play_result == Plays.run_yard[2]:
            print("You didnt gain any yards.")
            Plays.yards.append(Plays.run_yard[1])

        elif play_result == Plays.run_yard[3] or play_result == Plays.run_yard[4] or play_result == Plays.run_yard[5]:
            print("Solid run! You gained 5 yards.")
            Plays.yards.append(Plays.run_yard[3])

        elif play_result == Plays.run_yard[6] or play_result == Plays.run_yard[7]:
            print("Good blocking! You gained 7 yards.")
            Plays.yards.append(Plays.run_yard[6])

        elif play_result == Plays.run_yard[8] or play_result == Plays.run_yard[9]:
            print("Fantastic execution! You gained 10 yards.")
            Plays.yards.append(Plays.run_yard[8])

        elif play_result == Plays.run_yard[10]:
            print("Amazing run for a touchdown!!! You won the game!!!")
            exit()

        global yards_left
        Plays.yards_left -= Plays.yards[-1]
        print(f"You have {Plays.yards_left} yards to go.")




    def play_four(self):
        play_result = random.choice(Plays.quick_yard)

        if Plays.def_play == Plays.defense_play[0]:
            play_result = Plays.quick_yard[5]
            Plays.yards.append(Plays.quick_yard[5])

        if Plays.def_play == Plays.defense_play[2]:
            play_result = Plays.quick_yard[0]
            Plays.yards.append(Plays.quick_yard[0])

        print("You are running a quick pass")

        if play_result == Plays.quick_yard[0]:
            print("Tight window throw but it was incomplete.")
            Plays.yards.append(Plays.quick_yard[0])


        elif play_result == Plays.quick_yard[1]:
            print("That was a tough completion for 2 yards.")
            Plays.yards.append(Plays.quick_yard[1])


        elif play_result == Plays.quick_yard[2] or play_result == Plays.quick_yard[3] or play_result == Plays.quick_yard[4]:
            print("That was a great gain of 5 yards let's keep doing that.")
            Plays.yards.append(Plays.quick_yard[2])


        elif play_result == Plays.quick_yard[5] or play_result == Plays.quick_yard[6] or play_result == Plays.quick_yard[7] or play_result == Plays.quick_yard[8] or play_result == Plays.quick_yard[9]:
            print("Good job by the reciever making that guy miss for a gain of 7.")
            Plays.yards.append(Plays.quick_yard[5])


        elif play_result == Plays.quick_yard[10]:
            print("Best throw of the night for a gain of 10.")
            Plays.yards.append(Plays.quick_yard[10])


        elif play_result == Plays.quick_yard[11]:
            print("Amazing play by the reciever making multiple guys miss and scoring a touchdown to win the game!!!")
            exit()

        global yards_left
        Plays.yards_left -= Plays.yards[-1]
        print(f"You have {Plays.yards_left} yards to go.")