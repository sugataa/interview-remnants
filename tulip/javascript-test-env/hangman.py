import string
class Hangman():
    def __init__(self):
        self.word = 'testing'
        self.word_array = ['_', '_', '_', '_', '_', '_', '_']
        self.guesses = 5
        self.user_guesses = []
        while self.guesses != 0:
            # if the word array does not contain any _, end the game
            if '_' not in self.word_array:
                print('Correct!')
                return

            # check the user's guess against the word given
            # don't allow previous guesses
            user_guess = self.getGuess()

            # if the char is not in the word:
            print(user_guess)
            if user_guess not in self.word:
                # decrement the guesses if the user chooses an incorrect character
                self.guesses -= 1
                self.user_guesses.append(user_guess)
            else:
                # if the char is in the word, replace the index with the user's guess
                self.user_guesses.append(user_guess)
                for entry in enumerate(self.word):
                    if entry[1] == user_guess:
                        self.word_array[entry[0]] = user_guess


            # output current state
            print('Current state: ', " ".join(self.word_array))
            print('You have {} guesses left'.format(self.guesses))

    def getGuess(self):
        while True:
            self.user_guess = input('Enter your guess: ').strip()

            if len(self.user_guess) != 1 or self.user_guess not in string.ascii_lowercase or self.user_guess in self.user_guesses:
                print('Please enter 1 character in the lowercase alphabet from a to z that you have not entered before')
                print('Current state: ', " ".join(self.word_array))
                print('You have {} guesses left'.format(self.guesses))
            else:
                break
        return self.user_guess

Hangman()
