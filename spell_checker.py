from autocorrect import Speller

spell = Speller(lang='en')

def spell_checker(word):
    return spell(word)