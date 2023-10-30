from spellchecker import SpellChecker
def correct_text(input_text):
    spell = SpellChecker()
    words = input_text.split()
    new_words = []
    for word in words:
        if spell.unknown([word]):
            new_word = spell.correction(word)
            new_words.append(new_word)
        else:
            new_words.append(word)
    corrected_spelling = ' '.join(new_words)
    return corrected_spelling


# input_text = "this is wronng sspellingg of giwen textt inputt"
input_text = (input("enter text"))
print(input_text)
corrected_spelling = correct_text(input_text)
print(corrected_spelling)