def order(sentence):
    if sentence == "":
        return ""
    splitted_words = sentence.split(' ')
    mySet = {}
    for pos in splitted_words:
        splitted_word = list(pos)
        number = ''
        for letter in splitted_word:
            if letter.isdigit():
                number += letter
        mySet[number] = pos
    sortedSet = sorted(mySet.items(), key=lambda x: int(x[0]))
    return ' '.join(list(map(orderPhrasis, sortedSet)))


def orderPhrasis(e):
    return e[1]