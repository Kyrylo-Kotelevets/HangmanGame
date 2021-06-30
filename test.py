from hangman import Hangman

hg = Hangman()

while hg.game_over is None:
    print(hg.mask, hg.lives)

    letter = input()
    if hg.guess_the_letter(letter):
        print('Correct!')
    else:
        print('Wrong!')

print(hg.word)
