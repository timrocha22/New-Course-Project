print("Hello. Today I will be telling you a story about a curious cat.")
print("Please answer these questions before we start.")
print("\nPress enter after you answer my questions.")
input("Press 'enter' to continue.")

userName = input("\nWhat is your name?    ")
friendsName = input("\nWhat is your best friends name?    ")
cityName = input("\nName a city you would like to visit:    ")
userColor = input("\nWhat is your favorite color?    ")
userNum = input("\nPick any number:    ")

print("\nStory time!")

print("\nOne day, shortly after moving to", cityName, friendsName, "decided to explore the new neighborhood.")
print("During his exploration,", friendsName, "hears a bird chirping.") 
print("After curiously looking around, he spots a", userColor, "bird sitting on the windowsill of a house.")
print("\nShould", friendsName, "play with the bird?")

decision1 =input("Type yes or no:   ").lower()
if decision1 == 'yes':
    print("\nExcited,", friendsName, "climbs the closest tree and jumps through the window.",
    "To his surprise, there were", userNum, "birds of many different colors.",
    friendsName, "jumps around playing with them, while knocking over all the furniture.",
    "The owner of the house hears the ruckus and runs into the room.",
    "She sees", friendsName, "and angrily chases him out",
    friendsName, "barely escapes out of the window and down the tree.")
else:
    print("\nAfter thoughtful consideration, further exploration sounds more interesting.")

print("\n", friendsName, "continues to explore", cityName, "and spots a small pond.")
print(friendsName, "is parched after all the excitement.")
print("Should", friendsName, "go to the pond for a drink?")

decision2 = input("Type yes or no:  ").lower()
if decision2 == 'yes':
    print("\nSlowly,",friendsName, "approaches the pond for a drink and notices", userNum, "fish in the pond.",
    friendsName, "ignores them and goes for a drink when he gets splashed by the fish.",
    "so he jumps at them angrily and falls in the pond.",
    "Finally making its way out of the pond,", friendsName, "lays in the sun to dry off and warm up.")
else:
    print("\nHesitantly,", friendsName, "continues to explore the city, even though the street lights turned on. {- u O}")

if (decision1 == 'yes') and (decision2 == 'yes'):
    ending = 'bad'
    print("The owner of the birds was so upset, she called animal control.",
          "While", friendsName, "was drying off, he was spotted and aproached by the officer.",
          "Terrified of the stranger,", friendsName, "must make a split second decision!",
          "Should", friendsName, "run away from the officer?")
    decision3 = input("Type yes or no:   ").lower()
    if decision3 == 'yes':
        print("\nUnsure of what to do, he slowly aproaches the officer.",
              "luckily,", userName, "put his colllar on, so the officer was able to call his owner and return home safely.")
    else:    
        print("\nScared,", friendsName, "jumps a brick wall and runs away",
              "unfortunately he doesn't know where he runs to and is lost!",
              "After", usernum, "days being lost,", userName, "finds him walking on the sidewalk while going on lunch.",
              "So they both return home, excited to be reunited.", friendsName, "doesn't go too far from the house to this day.")

elif (decision1 == 'no') and (decision2 == 'no'):
    ending = 'good'
    print("\nAfter an adventurous day,", friendsName, "calls it a day and heads back home.",
          "he is very hungry so he bugs", friendsName, "and gets a juicy can of salmon.")

