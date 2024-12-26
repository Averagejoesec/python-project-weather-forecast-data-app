text = "Hello, how many vowels are in this sentence?"


def count_vowels(text):
    vowels = "aeiou"
    text.lower()
    count = 0
    for i in text:
        if i in vowels:
            count += 1
    message = f"The number of vowels in the string is: {count}"
    return print(message)

count_vowels(text)