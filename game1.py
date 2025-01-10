def adventure_game():
  """
  A simple text-based adventure game.
  """
  print("You find yourself in a dark forest. A path leads north and south.")
  choice1 = input("Do you go north or south? (north/south): ").lower()

  if choice1 == "north":
    print("You encounter a fearsome dragon guarding a cave.")
    choice2 = input("Do you fight the dragon or try to sneak past? (fight/sneak): ").lower()
    if choice2 == "fight":
      print("You bravely fight the dragon, but it's too powerful. You lose.")
    elif choice2 == "sneak":
      print("You carefully sneak past the dragon and find a hidden treasure chest filled with gold!") 
    else:
      print("Invalid choice. You stand frozen in fear and are eaten by the dragon.")
  elif choice1 == "south":
    print("You come to a river. A small boat is tied to the bank.")
    choice3 = input("Do you try to swim across or use the boat? (swim/boat): ").lower()
    if choice3 == "swim":
      print("You attempt to swim across, but the current is too strong. You're swept away.")
    elif choice3 == "boat":
      print("You use the boat to safely cross the river and reach a peaceful village.")
    else:
      print("Invalid choice. You hesitate too long and are attacked by river monsters.")
  else:
    print("Invalid choice. You wander aimlessly and are lost forever.")
    print("\nMap of your adventure:")
    print("1. Room 1 - The Village Square")
    print("2. Room 2 - Dark Forest")
    print("3. Room 3 - Hidden Cave")
    print("4. Room 4 - Mysterious Lake")
    print("5. Room 5 - Treasure Chamber")
    print("Your current position: " + current_room)

def pick_item():
    global inventory
    item = random.choice(["Sword", "Shield", "Health Potion", None])
    if item:
        print(f"\nYou found a {item}!")
        inventory.append(item)
    else:
        print("\nYou found nothing. Keep moving forward!")

def move_left():
    global current_room
    if current_room == "Room 1":
        current_room = "Room 5"
        print("\nYou move left and enter Room 5, the Treasure Chamber!")
    elif current_room == "Room 2":
        current_room = "Room 1"
        print("\nYou move left and return to the Village Square.")
    elif current_room == "Room 3":
        current_room = "Room 2"
        print("\nYou move left and find yourself back in the Dark Forest.")
    elif current_room == "Room 4":
        current_room = "Room 3"
        print("\nYou move left into the Hidden Cave.")
    elif current_room == "Room 5":
        print("\nYou're already in the Treasure Chamber! No more left turns.")
    else:
        print("\nInvalid direction.")

def move_right():
    global current_room
    if current_room == "Room 1":
        current_room = "Room 2"
        print("\nYou move right and enter the Dark Forest.")
    elif current_room == "Room 2":
        current_room = "Room 3"
        print("\nYou move right and find yourself in a Hidden Cave.")
    elif current_room == "Room 3":
        current_room = "Room 4"
        print("\nYou move right and arrive at a Mysterious Lake.")
    elif current_room == "Room 4":
        current_room = "Room 5"
        print("\nYou move right and discover the Treasure Chamber!")
    elif current_room == "Room 5":
        print("\nYou can't move right anymore. You're already at the treasure!")
    else:
        print("\nInvalid direction.")


    if current_room == "Room 2":
        print("\nIn the Dark Forest, you hear a rustling sound... A wild wolf appears!")
        action = input("Do you want to 'fight' or 'run'? ").lower()
        if action == "fight" and "Sword" in inventory:
            print("\nYou bravely fight the wolf with your Sword and win the battle!")
        elif action == "run":
            print("\nYou run away and escape safely!")
        else:
            print("\nYou don't have any weapon to fight! The wolf attacks you.")
            print("You lose the game.")
            exit()

def start_game():
    print("Welcome to the Adventure Game!")
    print("Your goal is to explore different rooms and reach the Treasure Chamber.")
    print("You can move by typing 'right' or 'left', and sometimes you will encounter challenges.")
    print("Good luck on your adventure!")

    global current_room
    global inventory
    current_room = "Room 1"  # Start in Room 1
    inventory = []

    while True:
        show_map()
        pick_item()

        # Encounter check for the Dark Forest (Room 2)
        encounter()

        # Take player's direction input
        choice = input("\nWhich direction would you like to go? (right/left): ").lower()

        if choice == "left":
            move_left()
        elif choice == "right":
            move_right()
        else:
            print("\nInvalid input. Please type 'right' or 'left'.")
        
        # Check if player reached the Treasure Chamber (Room 5)
        if current_room == "Room 5":
            print("\nCongratulations! You've found the Treasure and won the game!")
            break  # End the game

# Start the adventure game
start_game()


# Start the game
adventure_game()