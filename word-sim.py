import matplotlib.pyplot as plt
import random

class wordle_sim:
    def __init__(self):
        self.current_guess = ""
        self.closest_word = ""
        self.curr_guess_status = ["R"] * 5

    def getCurrGuessStatus(self):
        return self.curr_guess_status
    
    def getCurrentGuess(self):
        return self.current_guess
    
    def getClosestWord(self):
        return self.closest_word
    
    def setCurrGuessStatus(self, guess_status):
        self.curr_guess_status = guess_status

    def setCurrentGuess(self, guess):
        self.current_guess = guess

    def setClosestWord(self, word):
        self.closest_word = word

    def rando_letter(self):
        index = random.randint(1, 26)
        letter = chr(index + 96)
        return letter
    
    def rando_letter_v2(self):
        """ 
        Chances taken from: https://mathcenter.oxford.emory.edu/site/math125/englishLetterFreqs/
        The higher the chance, the more likely for the letter to get picked.
        """
        letters = "abcdefghijklmnopqrstuvwxyz"
        letters_freq = [0.08167, 0.09659, 0.12441, 0.16694, 0.29396, 0.31624, 0.33639, 0.39733, 
                        0.46699, 0.46852, 0.47624, 0.51649, 0.54055, 0.60804, 0.68311, 0.70240,
                        0.70335, 0.76322, 0.82649, 0.91705, 0.94463, 0.95441, 0.97801, 0.97951,
                        0.99925, 1]
        rng = random.random()
        rng = round(rng, 5)
        
        for i in range(26):
            if rng < letters_freq[i]:
                return letters[i]

    def rando_vowel(self):
        vowels = "aeiou"
        return random.choice(vowels)
    
    def rando_vowel_v2(self):
        """ 
        Chances taken from: https://mathcenter.oxford.emory.edu/site/math125/englishLetterFreqs/
        The higher the chance, the more likely for the vowel to get picked.
        """
        vowels = "aeiou"
        vowel_freq = [0.21436, 0.54774, 0.730578, 0.92761, 1]
        rng = random.random()
        rng = round(rng, 5)
        
        for i in range(5):
            if rng < vowel_freq[i]:
                return vowels[i]

    def rando_consonant(self):
        consonants = "bcdfghjklmnpqrstvwxyz"
        return random.choice(consonants)
    
    def rando_plural_consonant(self):
        # Generates consonants that can only be turned to plural by adding '-es'.
        consonants = "sxz"
        return random.choice(consonants)
    
    def rando_consonant_v2(self):
        """ 
        Chances taken from: https://mathcenter.oxford.emory.edu/site/math125/englishLetterFreqs/
        The higher the chance, the more likely for the consonant to get picked.
        """
        consonants = "bcdfghjklmnpqrstvwxyz"
        cons_freq = [0.02410, 0.06905, 0.13776, 0.17375, 0.20630, 0.30475, 0.30723, 0.31670,
                    0.38472, 0.42359, 0.53263, 0.56379, 0.56532, 0.66205, 0.76426, 0.91056,
                    0.94869, 0.95111, 0.98300, 1]
        
        rng = random.random()
        rng = round(rng, 5)

        for i in range(21):
            if rng < cons_freq[i]:
                return consonants[i]
            
            if rng < cons_freq[i]:
                return consonants[i]
    
    def strat_1(self):
        """
        This strategy aims to start generating two vowels in the middle three letters
        as vowels tend to be in the middle of a word. Then, consonants are generated
        to complete the word.
        """

        guess = "     "
        empty_letters = [0, 1, 2, 3, 4]
        mid_position = [1, 2, 3]

        mid_vowel = self.randomize_vowels()
        position = random.randint(1, 3)
        empty_letters.remove(position)
        mid_position.remove(position)
        guess = self.replace_char_at_index(mid_vowel, guess, position)
        
        mid_vowel = self.randomize_vowels()
        mid_vowel = self.rando_vowel()
        rng_index = random.randint(0, 1)
        empty_letters.remove((mid_position[rng_index]))
        guess = self.replace_char_at_index(mid_vowel, guess, mid_position[rng_index])
        
        for i in empty_letters:
            consonant = self.randomize_consonants()
            consonant = self.rando_consonant()
            guess = self.replace_char_at_index(consonant, guess, i)

        print("Guessed word: " + guess)
        self.check_closest_word(guess)

    def improved_strat_1(self):
        """
        This strategy is modified from strat_1() by using a letter generator that uses
        the frequency of letters in words as part of its letter generation. If the 
        letter appears in more words, it is more likely to get picked.
        """

        guess = "     "
        empty_letters = [0, 1, 2, 3, 4]
        mid_position = [1, 2, 3]

        mid_vowel = self.rando_vowel_v2()
        position = random.randint(1, 3)
        empty_letters.remove(position)
        mid_position.remove(position)
        guess = self.replace_char_at_index(mid_vowel, guess, position)
        
        mid_vowel = self.rando_vowel_v2()
        rng_index = random.randint(0, 1)
        empty_letters.remove((mid_position[rng_index]))
        guess = self.replace_char_at_index(mid_vowel, guess, mid_position[rng_index])
        
        for i in empty_letters:
            consonant = self.rando_consonant_v2()
            guess = self.replace_char_at_index(consonant, guess, i)

        print("Guessed word: " + guess)
        self.check_closest_word(guess)

    def strat_2(self):
        """
        This strategy aims to create a four-letter word and add the consonant 's' to
        to form the plural of the four-letter word.
        """

        guess = "    s"
        empty_letters = [0, 1, 2, 3]

        mid_vowel = self.randomize_vowels()
        position = random.randint(0, 1) + 1
        empty_letters.remove(position)
        guess = self.replace_char_at_index(mid_vowel, guess, position)
        
        for i in empty_letters:
            consonant = self.rando_consonant_v2()
            guess = self.replace_char_at_index(consonant, guess, i)

        print("Guessed word: " + guess)
        self.check_closest_word(guess)

    def replace_char_at_index(self, to_replace, word, index):
        new_word = word[: index] + to_replace + word[index + 1 :]
        return new_word
    
    def check_closest_word(self, guess):
        # Finds the word closest to the guess.
        word_file = open("five-letter-words.txt", "r")
        words = word_file.readlines()
        best_word = ""
        best_guess = ["R"] * 5

        print("Checking guess...")

        for curr_word in words:
            curr_guess = self.check_word(guess, curr_word)

            G_currGuess = curr_guess.count("G")
            Y_currGuess = curr_guess.count("Y")
            G_bestGuess = best_guess.count("G")
            Y_bestGuess = best_guess.count("Y")
            
            if G_currGuess > G_bestGuess:
                best_word = curr_word
                best_guess = curr_guess
                continue
            elif G_currGuess == G_bestGuess:
                if Y_currGuess > Y_bestGuess:
                    best_word = curr_word
                    best_guess = curr_guess
                    continue
        
        self.setCurrentGuess(guess)
        self.setClosestWord(best_word[: -1])
        self.setCurrGuessStatus(best_guess)

        print("Closest Word: " + self.getClosestWord())
        print("Current Guess Status: ", end = " ")
        print(self.getCurrGuessStatus())
        print("Greens: " + str(self.getCurrGuessStatus().count("G")), end = ", ")
        print("Yellows: " + str(self.getCurrGuessStatus().count("Y")), end = "\n\n")
        word_file.close()

    def modified_strategy_1(self):
        """
        Strategy 1 is modified to have the probabilities of letters in the dictionary accounted for.
        """


    def check_word(self, guess, target_word):
        letters_checked = []
        guess_status = ["R"] * 5
        if guess == target_word:
            guess_status = ["G"] * 5
        else:
            for i in range(5):
                if guess[i] == target_word[i]:
                    guess_status[i] = "G"
                    letters_checked.append(guess[i])
            
            for j in guess:
                if j in letters_checked:
                    continue
                elif j in target_word:
                    guess_status[i] = "Y"
                else:
                    guess_status[i] = "R"
                letters_checked.append(guess[i])
        return guess_status



if __name__ == "__main__":
    first_simulation = wordle_sim()
    print(first_simulation.randomize_vowels_v2())
    first_simulation.strat_1()
    first_simulation.strat_2()
