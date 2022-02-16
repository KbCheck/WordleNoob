import string


class WordleSpace:

    def __init__(self, ans):
        # The five letters that make up a wordle word. Contains all the remaining valid letters.
        self.possibles = list(string.ascii_lowercase)
        self.known = ["","","","",""]
        self.contains = []     #Contains any letters that have been found but do not yet have a place.
        self.guesses = []      #Contains all guesses given
        self.ans = ans         #The answer to given wordle problem.
        self.isSolved = False  #The solved state for the current problem.
    
    ##################
    ### OPERATIONS ###
    ##################

    def __yellow(self, char):
        #Add character to contains
        if not char in self.contains: 
            self.contains.append(char)
    
    def __green(self, pos, char):
        #set character in position as known
        self.known[pos] = char
        #Remove character from contains
        if char in self.contains:
            self.contains.remove(char)

    def __grey(self, char):
        #remove character from possibles
        if char in self.possibles:
            self.possibles.remove(char)

    def guess(self, guess):
        response = []  # list of results for each character
        self.guesses.append(guess)
        if guess == self.ans:
            self.isSolved = True
        #Iterate through guess and resolve
        for i in range(0,len(self.known)):
            if guess[i] == self.ans[i]:  #letter in correct spot
                response.append("G")
                self.__green(i,guess[i])
            elif guess[i] in self.ans:   #letter exists but not in correct spot
                response.append("Y")
                self.__yellow(guess[i])
            else:                        #letter not in answer at all
                response.append("R")
                self.__grey(guess[i])
        return response

    #############
    ## GETTERS ##
    #############

    def isKnown(self, pos):
        return len(self.possibles[pos]) == 1

    def numGuesses(self):
        return len(self.guesses)

    def getGuesses(self):
        return self.guesses

    def solved(self):
        return self.isSolved


    ##########
    # STATIC #
    ##########

    def acceptable(guess):
        accept = False  
        if len(guess) == 5:
            isAlpha = True
            for char in guess:
                if not char.isalpha():
                    isAlpha = False
            if isAlpha:
                accept = True
        return accept

    def visualize(guess, response):
        visual = ""
        for i in range(0, len(guess)):
            match response[i]:
                case 'G':
                    visual += '\x1b[6;30;42m' +" "+ guess[i] +" "+ '\x1b[0m' + " "
                case 'Y':
                    visual += '\x1b[6;30;43m' +" "+ guess[i] +" "+ '\x1b[0m' + " "
                case 'R':
                    visual += '\x1b[6;30;47m' +" "+ guess[i] +" "+ '\x1b[0m' + " "
        return visual


    

        
#############
## TESTING ##
#############

if "__main__" == __name__:
    
    #Get the word to try solve and create the wordle instance
    accept = False
    while not accept:
        problem = input("Provide answer: ")
        accept = WordleSpace.acceptable(problem)
    wordle = WordleSpace(problem.lower())

    while not wordle.solved():
        #Get the next guess
        accept = False
        while not accept:
            guess = input("Next guess: ")
            accept = WordleSpace.acceptable(guess)
        response = wordle.guess(guess.lower())
        print(WordleSpace.visualize(guess, response))

    print("Wordle solved!")
    
    