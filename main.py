### SHOPPING LIST GAME ###
## By Lachlan and Brodie ##

### The program will allow the user to display the shopping list and modify the shopping list by adding or removing items. There are also two games to play using lists. The memory game asks the user to memorize their shopping list and recount all their items. The spot the difference game shows the user a list of items and after 10 seconds the list changes. The user needs to input the 3 items that changed. You can also exit the program.


# imports for clear console, random number, time and coloured text
import os 
import random
import time
from simple_colors import *

# Clear Console Function clears the console of text. It wipes and 'refreshes' the screen.
def clearConsole():
  os.system("clear")

# Display shopping list shows each item on the list on a seperate line
def display_shopping_list(shopping_list):
    if not shopping_list:
        print(red("Your shopping list is empty.\n"))
    else:
      print(blue("Your Shopping list: "))
      for item in shopping_list:
        print(item)

# Adds item to shopping list
def add_item(shopping_list):
    addlist = input("What item would you like to add? ")
    print(blue(f"Added {addlist} to your Shopping List."))
    shopping_list.append(addlist)

# Deletes item from shopping list
def delete_item(shopping_list):
    if len(shopping_list) == 0:
      print(red("Your shopping list is empty.\n"))
      return
    display_shopping_list(shopping_list)
    index = input("Enter the number of the item you want to delete (or 'q' to cancel): ")
    if index == 'q':
        return
    try:
        index = int(index)
        if index < 1 or index > len(shopping_list):
            print(red("Invalid index."))
        else:
            item = shopping_list.pop(index - 1)
            print(blue(f"{item} has been removed from the shopping list."))
    except ValueError:
        print(red("Invalid input. Enter a valid index or 'q' to cancel."))

# The memory game asks the user to memorize their shopping list and recount all their items
def memoryGame(shopping_list):
  if len(shopping_list) == 0:
      print(red("Your shopping list is empty.\n"))
      return
  display_shopping_list(shopping_list)
  print("\n")
  time.sleep(10)
  clearConsole()
  score = 0
  guesses = len(shopping_list)
  guessedlist = []
  for i in range(len(shopping_list)):
    itemchoice = input(f"Choice {i+1}: ")
    if itemchoice in shopping_list:
      if itemchoice in guessedlist:
        print(red("Already guessed. Try again"))
        while itemchoice in guessedlist:
          itemchoice = input(f"Choice {i+1}: ")
      else:
        score = score + 1
        guessedlist.append(itemchoice)
    guesses = guesses - 1
    if guesses == 0:
      break
  correct = len(guessedlist)
  length = len(shopping_list)
  print(green(f"You got {correct} correct out of {length}"))

# Spot the difference game
def STD(): # Spot the Difference game
  score = 0 # Score to 0
  game_list = ['apple','banana','cake','donut','egg','fish','grape','ham','ice','jam','kiwi','lemon','melon','nut','orange','pizza','quiche','rice','sushi','turkey','utensil','vinegar','waffle','yogurt','zucchini']
  ## Game list length = 25
  
  
  STDGuessed = [] ## List of guessed items empty
  Random10List = [] ## List of 10 random items empty
  print(blue("Please memorise the items on the list\nYou have 10 seconds\n"))
  for i in range(10): #Randomly selects 10 words and adds them to a different list
    number = random.randint(1,len(game_list)) ## Number = random number from 1 to 10
    Random10List.append(game_list[number - 1]) 
    game_list.pop(number - 1)
  for i in range(len(Random10List)): #Prints each selected item chosen for the random list
    print(Random10List[i]) #Prints random list of 10
  time.sleep(10) ## Waits 10 seconds
  clearConsole() #Clears the r=random list of chosen words

  

  
  RandomNumber11 = random.randint(1,len(Random10List)) # Random number 1 to 10 for random list
  RandomNumber12 = random.randint(1,len(game_list)) # Random number 1 to 25 for game list
  while RandomNumber12 in Random10List:
    RandomNumber12 = random.randint(1,len(game_list)) # Get another Random number 1 to 25 for game list
 
  Random10List[RandomNumber11 - 1] = game_list[RandomNumber12 - 1]
  Changed1 = Random10List[RandomNumber11 - 1] 

  RandomNumber21 = random.randint(1,len(Random10List)) # Random number 1 to 10 for random list
  RandomNumber22 = random.randint(1,len(game_list)) # Random number 1 to 25 for game list
  while RandomNumber22 in Random10List:
    RandomNumber22 = random.randint(1,len(game_list)) # Get another Random number 1 to 25 for game list

  Random10List[RandomNumber21 - 1] = game_list[RandomNumber22 - 1]
  Changed2 = Random10List[RandomNumber21 - 1] 

  RandomNumber31 = random.randint(1,len(Random10List)) # Random number 1 to 10 for random list
  RandomNumber32 = random.randint(1,len(game_list)) # Random number 1 to 25 for game list
  while RandomNumber32 in Random10List:
    RandomNumber32 = random.randint(1,len(game_list)) # Get another Random number 1 to 25 for game list

  Random10List[RandomNumber31 - 1] = game_list[RandomNumber32 - 1]
  Changed3 = Random10List[RandomNumber31 - 1] 

  print(blue("Please type what items have changed\nThree items have been replaced\n"))
  
  for i in range(len(Random10List)):
    print(Random10List[i])

  
  
  print("\n")
  for i in range(3):
    itemchoice = input(f"Choice {i+1}: ")
    if itemchoice == Changed1: 
      score = score + 1
      STDGuessed.append(itemchoice)
      Changed1 = "random value that no one gonna guess" ## changes changed1 value to a value that they wont guess to cheat
    elif itemchoice == Changed2: 
      score = score + 1
      STDGuessed.append(itemchoice)
      Changed2 = "another random value no hacking pls" ## changes changed2 value to a value that they wont guess to cheat
    elif itemchoice == Changed3: 
      score = score + 1
      STDGuessed.append(itemchoice)
      Changed3 = "dont check the code to cheat thats naughty" ## changes changed3 value to a value that they wont guess to cheat

  
  

  print(green(f"You got {score} correct out of 3"))

  if score == 3:
    print(green("\nCongratulations! You win!"))

# main code runs until you exit
def main():
    shopping_list = ["apple", "banana", "orange"] #####
    while True:
        print("\n1. Display shopping list")
        print("2. Add item")
        print("3. Delete item")
        print("4. Memory game")
        print("5. Spot the difference Game")
        print("6. Quit")
        choice = input("Enter your choice: ")
        clearConsole()
        if choice == '1':
          display_shopping_list(shopping_list)
        elif choice == '2':
          add_item(shopping_list)
          
        elif choice == '3':
          delete_item(shopping_list)
        elif choice == '4':
          memoryGame(shopping_list)
        elif choice == '5':
          STD()
        elif choice == '6':
          print(green("Thanks for shopping at Coles"))
          break
        else:
          print(red("Invalid choice. Please try again."))
        

main()


