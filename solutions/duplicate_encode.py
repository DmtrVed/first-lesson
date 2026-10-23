def duplicate_encode(text):
    otvet = []
    text1 = [word.lower() for word in text]
    for i in range(len(text1)):
        if text.count(text1[i]) > 1:
            otvet += [')']
        if text.count(text1[i]) == 1:
            otvet += ['(']
    sentence = "".join([f"{word}" for word in otvet])
    return sentence