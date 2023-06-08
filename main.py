### SHOPPING LIST GAME ###
## By Lachlan and Brodie ##

#  
#  
#  
#  
#  



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
  
  
  STDGuessed = [] ## List of guessed items empty
  Random10List = [] ## List of 10 random items empty
  print("Please memorise the items on the list\nYou have 10 seconds\n")
  for i in range(10): #Randomly selects 10 words and adds them to a different list
    number = random.randint(1,len(game_list)) ## Number = random number from 1 to 10
    Random10List.append(game_list[number - 1]) 
    game_list.pop(number - 1)
  for i in range(len(Random10List)): #Prints each selected item chosen for the random list
    print(Random10List[i]) #Prints random list of 10
  time.sleep(10) ## Waits 15 seconds
  clearConsole() #Clears the r=random list of chosen words

  
  #Changed1 = random.randint(1,len(Random10List)) ## Changed 1 = random number from 1 to 10
  #ChangedTo1 = random.randint(1,len(game_list))



  
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

  print("Please type what items have changed\nThree items have been replaced\n")
  
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
      Changed2 = "another random value no hacking pls" ## changes changed1 value to a value that they wont guess to cheat
    elif itemchoice == Changed3: 
      score = score + 1
      STDGuessed.append(itemchoice)
      Changed3 = "dont check the code to cheat thats naughty" ## changes changed1 value to a value that they wont guess to cheat

  
  

  print(f"You got {score} correct out of 3")

  if score == 3:
    print("Congratulations! You win!")


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


