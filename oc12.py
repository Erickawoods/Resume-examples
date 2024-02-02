# Your challenge tonight is to write a basic adventure game using some of the  
#code provide below and using if/elif statments

import random


yes_no = ["yes", "no"]
directions = ["left", "right", "forward", "backward"]
 
# Introduction
name = input("What is your name, adventurer?\n")
print("Greetings, " + name + ". Let us go on a quest!")
print("You find yourself on the edge of an enchanted forest.")
print("Can you find your way through?\n")
 
# Start of game
response = ""
while response not in yes_no:
    response = input("Would you like to step into the enchanted forest?\nyes/no\n")
    if response == "yes":
        print("You head into the enchanted forest. You hear Ewoks in the distance.\n")
    elif response == "no":
        print("You are not ready for this quest. Goodbye, " + name + ".")
        quit()
    else: 
        print("I didn't understand that.\n")
 
# Next part of game
response = ""
while True:
    print("To your left, you see a storm trooper.")
    print("To your right, there is more forest.")
    print("There is a stone fence directly in front of you.")
    print("Behind you is the forest exit.\n")
    response = input("What direction do you move?\nleft/right/forward/backward\n")
    if response == "left":
        print("You encounter a storm trooper, what do you do?")
        fight = input("fight the storm trooper? y/n\n")
        if  fight == "y":
            print("10 sided dice rolled to see if you beat the storm trooper you need a 5 or higher")
            number = random.randint(1, 10)
            if number >= 5:
                print(f"You have defeated the storm trooper with a roll of {number} and escaped the enchanted forest with grogu")
                response = ""
            else: print("You rolled less than 5 the storm trooper kills you with his hands") 
            quit()
        else: print("You ran away")
        
    elif response == "right":
        print("You head deeper into the forest.  You find a hut in front of you.\n")
        hut = input("You enter the hut do you go left or right?\n")
        if hut == "left":
            print("You fall through a trap door and find Kylo Ren. You find a blaster at your feet.")
            ren = input("\nDo you shoot Kylo Ren or do you run.  shoot/run\n")
            if ren == "shoot":
                blast = random.randint(1, 10)
                print("You try and shoot Kylo Ren with 70% accuracy")
                if blast <= 7:
                    print("You shoot Kylo Ren and escape the hut")
                    quit()
                else: print("You try and shoot Kylo Ren but miss and he chokes you with the force")
            else: print("You try and run from Kylo Ren but he catches you and throws you in the dungeon.")
            quit()
        else:  print("You head to the right and find a staircase and start to asscend you get to the top and find Princess Leia.\n")  
        princess = input("Do you try and save her?y/n\n")
        if princess == "y":
                print("You save Princess Leia and escape the hut")
        else: print("Princess Leia shoots you for not being part of the resistance ")
        quit()
    elif response == "forward":
        wall = input("You find a stone fence you can climb do you climb it?.y/n\n")
        if wall == "y":
            print("You scale the fence and find a Rancor")
            rancor = input("Do you charm the Rancor or run? c/r\n")
            if rancor == "c":
                print("You charm the Rancor and ride it to safety")
                quit()   
            else: print("The Rancor is not friendly and eats you")
            quit()
        else: print("You turn back and get lost and run into Chewbacca")
        print("He wants you to take a lightsaber to Yoda")
        lightsaber = input("Do you take the lightsaber from him? y/n\n")
        if lightsaber == "y":
            print("You take the lightsaber, a dice roll will determine if you help or kill Chewbacca.")
            lightsaber = random.randint(1, 10)
            if lightsaber >= 5:
                print(f"Your rolled a {lightsaber}")
                print("You kill Chewbacca and steal the lightsaber")
            else: print(f"You rolled a {lightsaber}. Chewbacca is greatful you did not try and steal the lightsaber and kill him so he leads you to the exit")
        else: print("Chewbacca knows you mean harm so he throws you into a Sarlacc pit to never been seen again") 
        
        response = "" 
    elif response == "backward":
            print("The carbonite door to the forest slams behind you and now you are stuck.")
            cave = input("Do you go to the cave or the tower?\n")
            if cave == "cave":
                print("You find Darth Vader in the cave creating a suit. You decide to team up with him to escape")
            else: print("You find Obi-Wan Kenobi and Luke Skywalker in the tower. They have killed all the bad creatures of the forest and want you to rule for them because they have to continue fighting the Empire")
    else:
        print("I didn't understand that.\n")
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
