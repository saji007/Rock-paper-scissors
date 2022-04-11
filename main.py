import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
game_images = [rock,paper,scissors]

user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# invalid check
if user_choice>=3 or user_choice <0:
  print("You typed an invalid number")
else:   
  print(game_images[user_choice])
  
  # computer choose  
  computer_choice = random.randint(0,2)
  print(f"Computer chose:\n{computer_choice}")
  print(game_images[computer_choice])
  
  # draw check
  if user_choice == computer_choice:
    print("It's a Draw")
    
  # win check
  elif user_choice ==0 and computer_choice==2:
    print("You win!")
  elif user_choice==1 and computer_choice==0:
    print("You win!")
  elif user_choice==2 and computer_choice==1:
    print("You win!") 
  else:
    print("You lose")
  