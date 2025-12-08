a = 12
b = 6

print(f"sum {a+b}")
print(f"difference {a-b}")
print(f"multiplication {a*b}")
print(f"division {a/b}")
print(f"remainder {a%b}")


# A function that count vowels
def vowel_couter(sentence):
    vowel = "aeiouAEIOU"
    count = 0
    for character in sentence:
        if character in vowel:
            count += 1
    return f"The number of vowel(s) is {count}"


# OR
def vowel_couters(sentence):
    vowel = "aeiouAEIOU"
    return sum(1 for character in sentence if character in vowel)


counter = vowel_couter("this is good,I love delicious food")
print(counter)
counters = vowel_couters("this is good,I love delicious food")
print(counter)


# palindrome checker
def palindrome_checker(word):
    if word == word[::-1]:
        return f"{word} is a palindrome"
    else:
        return f"{word} is not a palindrome"


pali = palindrome_checker("racecar")
print(pali)


# return the maximum number
def maximum(number):
    return max(number)
