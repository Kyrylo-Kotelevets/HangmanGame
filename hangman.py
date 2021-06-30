from word_generator import *


class Hangman:
    """ Class with main functions for Hangman game """
    FILLER = '_'

    def __init__(self):
        self.__game_over = None
        self.__word = list(get_random_word())
        self.__mask = [Hangman.FILLER] * len(self.__word)
        self.__guessed_letters = set()
        self.__wrong_letters = set()
        self.__lives = 7

    def guess_the_letter(self, letter: str) -> bool:
        """"""
        if self.__game_over is not None:
            raise Exception("Game overed")

        if not isinstance(letter, str) or len(letter) != 1 or letter.upper() not in ALPHABET:
            raise ValueError("Input letter (%s) must be single and russian" % letter)
        letter = letter.upper()

        if letter in self.__guessed_letters or letter in self.__wrong_letters:
            return False  # Maybe ERROR

        if letter in self.__word:
            for i, ltr in enumerate(self.__word):
                if ltr == letter:
                    self.__mask[i] = letter
            self.__guessed_letters.add(letter)
            if Hangman.FILLER not in self.__mask:
                self.__game_over = True
            return True

        self.__wrong_letters.add(letter)
        self.__lives -= 1
        if not self.__lives:
            self.__game_over = False
        return False

    def give_up(self):
        """ This method should be called when you decided to end game """
        if self.__game_over is not None:
            raise Exception("Game overed")
        self.__game_over = False

    @property
    def game_over(self):
        return self.__game_over

    @property
    def guessed_letters(self):
        return self.__guessed_letters

    @property
    def wrong_letters(self):
        return self.__wrong_letters

    @property
    def mask(self):
        return ''.join(self.__mask)

    @property
    def word(self):
        if self.__game_over is None:
            self.__game_over = False
        return ''.join(self.__word)

    @property
    def lives(self):
        return self.__lives
