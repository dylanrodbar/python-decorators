def get_capitalized_word(word):
    return word.capitalize()


def call_get_capitalized_word(function):
    word = "gaga"
    return function(word)

print(call_get_capitalized_word(get_capitalized_word))