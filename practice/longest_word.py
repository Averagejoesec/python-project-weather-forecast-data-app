words = ["apple", "banana", "cherry", "blueberry"]

def longest_word(words):
    longest_word = ''
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    word_length = len(longest_word)
    message = print(f"\"{longest_word}\" is the longest word with {word_length} characters.")
    return message


longest_word(words)