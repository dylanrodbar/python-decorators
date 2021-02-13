def get_capitalized_word(word):

    def capitalized_word(word):
        return word.capitalize()

    resulting_word = capitalized_word(word)
    return resulting_word


capitalize_func = get_capitalized_word
print(capitalize_func("gaga"))