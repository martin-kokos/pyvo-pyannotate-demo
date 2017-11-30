
def get_letter(word, n):
    return word[n]


def flip(word):
    flipped = []
    for i in range(len(word)):
        letter = get_letter(word, len(word) - i - 1)
        flipped.append(letter)
    return ''.join(flipped)
