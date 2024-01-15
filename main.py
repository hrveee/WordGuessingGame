# import random module
import random


# The initialize guessed_word function of the game
def init_guessed_word():
  """
  This function is used for initialized guessed_word."""

  # a list variable to store words to be guess
  words_list = [
      "apple", "banana", "orange", "grapes", "mango", "kiwi", "watermelon",
      "pineapple", "strawberry", "blueberry", "peach", "pear", "plum"
  ]

  # declaring guesses_word variable and the value is random choice from words_list
  guessed_word = random.choice(words_list)

  return guessed_word


# the start_game function is used to start the game
def start_game():
  """
  This function is used for start the game."""

  # declaring guessed_word variable and the value is main_system_of_game() function
  guessed_word = init_guessed_word()

  # declaring hint variable to give a clue for the player and the value (the first and the last alphabet) is get from guessed_word variable
  hint = guessed_word[0] + guessed_word[-1]

  # declaring store_guess_list variable in empty list value
  store_guess_list = []

  # declaring how many user can attempt to play the game
  attempt = 6

  # ask the user to enter his/her name and print the welcome message to screen
  player_name = input("Enter your name please: ")
  print(
      "\nHello {}, welcome to the game world! You only have 6 attempts to guess the word.\n"
      .format(player_name))

  # loop the game until the user guess the word or the user run out of attempts
  for guess in range(attempt):

    # ask the user to enter the guess letter and check if the user input valid or not
    while True:
      letter = input("Guess the letter: ")

      if len(letter) == 1:
        break
      else:
        print("Oops: Please Guess a letter!\n")

    # check if the guess letter is in the guessed_word variable
    if letter in guessed_word:
      print("Yes, your is right!")
      store_guess_list.append(letter)
    else:
      print("No, your answer is wrong!")

    # check if the user have run 3 attempt to guess the word and ask user if they want to get clue
    if guess == 3:

      # ask user if they want to get clue
      clue_request = input("\nDo you want a clue? (Y/N)")

      # if the user input "Y", then print the clue, otherwise print the message
      if clue_request.upper().startswith("Y"):
        print("Clue: the first letter and the last letter of the word is {}\n".
              format(hint))
      else:
        print("You're very confident!\n")

  # check how many player_user guess the word and print the store_guess_list
  print(
      "\nNow let's see what have you guessed so far. You have guessed: {} letters correctly"
      .format(len(store_guess_list)))
  print("These letters are: {}".format(store_guess_list))

  # ask the user to enter the whole guess word and check if the user answer is correct or incorrect
  word_guess = input("\nGuess the whole word: ")
  if word_guess.lower() == guessed_word:
    print("Congratulations! You have guessed the word correctly!")
  else:
    print("Sorry, the answer was {}".format(guessed_word))

  # print thank you message and exit the game
  print("\nThank you for playing this game")
  exit()


# run the program in main gate
if __name__ == "__main__":
  start_game()
