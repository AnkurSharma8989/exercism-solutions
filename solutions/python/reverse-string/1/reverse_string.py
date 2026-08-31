def reverse(text):
    reversetext = ""
    for reverse in range(len(text)-1, -1, -1):
        reversetext += text[reverse]
    return reversetext