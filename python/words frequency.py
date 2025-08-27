def long_word(text):
    words = text.split()
    longest = ""
    max_length = 0
    for word in words:
        if len(word) > max_length:
            max_length = len(word)
            longest = word
    print(f"The longest word is: {longest}\nAnd its length is: {max_length}")

text = input("Enter the text: ")
long_word(text)
