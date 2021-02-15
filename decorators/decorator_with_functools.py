import functools


def capitalize_decorator(function):

    @functools.wraps(function)
    def wrapper():
        function_value = function()
        capitalized_word = function_value.capitalize()
        return capitalized_word

    return wrapper


@capitalize_decorator
def get_my_fav_album_name():
    return "chromatica"


print(get_my_fav_album_name.__name__)

