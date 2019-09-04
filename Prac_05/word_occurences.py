word_to_count = {}
user_input = input("Enter text: ")
words = user_input.split()
for word in words:
    frequency = word_to_count.get(word, 0)
    word_to_count[word] = frequency + 1
words = list(word_to_count.keys())
words.sort()

print(word_to_count)

max_length = 0
for word in words:
    if len(word) > max_length:
        max_length = len(word)
for word in words:
    print("{:{}} : {}".format(word, max_length, word_to_count[word]))
