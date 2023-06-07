### SHOPPING LIST GAME ###
## By Lachlan and Brody ##
import os
import random
import time
def clearConsole():
  os.system("clear")
  
def display_shopping_list(shopping_list):
    if not shopping_list:
        print("Your shopping list is empty.\n")
    else:
      print("Your Shopping list: ") 
      for item in shopping_list:
        print(item)

def add_item(shopping_list):
    pass

def delete_item(shopping_list):
    display_shopping_list(shopping_list)
    index = input("Enter the number of the item you want to delete (or 'q' to cancel): ")
    if index == 'q':
        return
    try:
        index = int(index)
        if index < 1 or index > len(shopping_list):
            print("Invalid index.")
        else:
            item = shopping_list.pop(index - 1)
            print(f"{item} has been removed from the shopping list.")
    except ValueError:
        print("Invalid input. Enter a valid index or 'q' to cancel.")

def memoryGame(shopping_list):
  score = 0
  guesses = len(shopping_list)
  guessedlist = []
  for i in range(len(shopping_list)):
    itemchoice = input(f"Choice {i+1}: ")
    if itemchoice in shopping_list:
      if itemchoice in guessedlist:
        print("Already guessed. Try again")
        while itemchoice in guessedlist:
          itemchoice = input(f"Choice {i}")
      else:
        score = score + 1
        guessedlist.append(itemchoice)
    guesses = guesses - 1
    if guesses == 0:
      break
  correct = len(guessedlist)
  print(f"You got {correct} correct out of ", len(shopping_list))
  
def STD(): # Spot the Difference
  score = 0 # Score to 0
  game_list = ['apple','banana','cake','donut','egg','fish','grape','ham','ice','jam','kiwi','lemon','melon','nut','orange','pizza','quiche','rice','sushi','turkey','utensil','vinegar','waffle','yogurt','zucchini']
  ## Game list length = 25
  
  STDGuesses = 3 ## 3 guesses
  STDGuessed = [] ## List of guessed items empty
  Random10List = [] ## List of 10 random items empty
  for i in range(10): #Randomly selects 10 words and adds them to a different list
    number = random.randint(1,len(game_list)) ## Number = random number from 1 to 10
    Random10List.append(game_list[number - 1])
    game_list.pop(number - 1)
  for i in range(len(Random10List)):
    print(Random10List[i])
  time.sleep(15)
  clearConsole()
  
  added1 = random.randint(1,len(game_list))
  Random10List.append(game_list[added1 - 1])
  added2 = random.randint(1,len(game_list))
  Random10List.append(game_list[added2 - 1])
  
  removed = random.randint(1,len(game_list))
  Random10List.pop(removed)
  
  for i in range(len(Random10List)):
    print(Random10List[i])

  
  while True:
    itemchoice = input("Choice 1: ")
    if itemchoice == added1 or itemchoice == added2 or itemchoice == removed:
      if itemchoice in STDGuessed:
        print("Already guessed. Try again")
        while itemchoice in STDGuessed:
          itemchoice = input("Choice 1: ")
      else:
        score = score + 1
        STDGuessed.append(itemchoice)
    STDGuesses = STDGuesses - 1
    if STDGuesses == 0:
      break

    itemchoice = input("Choice 2: ")
    if itemchoice == added1 or itemchoice == added2 or itemchoice == removed:
      if itemchoice in STDGuessed:
        print("Already guessed. Try again")
        while itemchoice in STDGuessed:
          itemchoice = input("Choice 2: ")
      else:
        score = score + 1
        STDGuessed.append(itemchoice)
    STDGuesses = STDGuesses - 1
    if STDGuesses == 0:
      break
      
    itemchoice = input("Choice 3: ")
    if itemchoice == added1 or itemchoice == added2 or itemchoice == removed:
      if itemchoice in STDGuessed:
        print("Already guessed. Try again")
        while itemchoice in STDGuessed:
          itemchoice = input("Choice 3: ")
      else:
        score = score + 1
        STDGuessed.append(itemchoice)
    STDGuesses = STDGuesses - 1
    STDGuessed = STDGuessed + 1
    if STDGuesses == 0:
      break

  if len(STDGuessed) > 0:
    correct = len(STDGuessed)
  print(f"You got {correct} correct out of 3")


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
          addlist = input("What item would you like to add? ")
          print(f"Added {addlist} to your Shopping List.")
          shopping_list.append(addlist)
        elif choice == '3':
          delete_item(shopping_list)
        elif choice == '4':
          memoryGame(shopping_list)
        elif choice == '5':
          STD()
        elif choice == '6':
          print("Thanks for shopping at Coles")  
          break
        else:
          print("Invalid choice. Please try again.")
        

main()


