def palidromechecker(word):
    word = word.lower().replace(" ", "")
    return word == word[::-1]


print(palidromechecker("A man a plan a canal Panama"))


def reverse(sentence):
    words = sentence.split()
    reverse = " ".join(words[::-1])
    return reverse


print(reverse("good boy dude"))
