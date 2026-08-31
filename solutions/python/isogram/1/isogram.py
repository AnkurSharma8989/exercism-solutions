def is_isogram(phrase):
    for word in phrase.lower():
        if word in "abcdefghijklmnopqrstuvwxyz":
            count = (phrase.lower()).count(word)
            if count > 1:
                return False
            continue

    return True