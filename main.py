### SHOPPING LIST GAME ###
## By Lachlan and Brody ##
import os
import random
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
  
def STD():
  game_list = ['apple','banana','cake','donut','egg','fish','grape','ham','ice','jam','kiwi','lemon','melon','nut','orange','pizza','quiche','rice','sushi','turkey','utensils','vinegar','waffle','yogurt','zucchini']
  STDGuesses = len(game_list)
  STDGuessed = []
  STDGuess = input("STD? ")
  ### code here
  

def main():
    shopping_list = ["apple", "banana", "orange"] #####
    while True:
        print("1. Display shopping list")
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
          STD(shopping_list)
        elif choice == '6':
          print("Thanks for shopping at Coles")  
          break
        else:
          print("Invalid choice. Please try again.")
        

main()
