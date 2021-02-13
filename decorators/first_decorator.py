def get_my_fav_album_name():
    return "chromatica"


def capitalize_decorator(function):

    def wrapper():
        function_value = function()
        capitalized_word = function_value.capitalize()
        return capitalized_word

    return wrapper


decorate = capitalize_decorator(get_my_fav_album_name)
print(decorate())
