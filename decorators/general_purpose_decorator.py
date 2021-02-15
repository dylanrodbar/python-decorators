def capitalize_decorator(function):

    def wrapper(*args,**kwargs):
        print("positional arguments: ", args)
        print("keyboard arguments: ", kwargs)
        function_value = function(*args, **kwargs)
        capitalized_word = function_value.capitalize()
        return capitalized_word

    return wrapper


@capitalize_decorator
def get_my_fav_album_name(album):
    return album


print(get_my_fav_album_name("chromatica"))
print(get_my_fav_album_name(album="chromatica"))

