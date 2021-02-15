def capitalize_decorator_with_arguments(arg1, arg2):
    def capitalize_decorator(function):

        def wrapper(*args,**kwargs):
            print("positional arguments: ", args)
            print("keyboard arguments: ", kwargs)
            print(arg1.capitalize())
            print(arg2.capitalize())
            function_value = function(*args, **kwargs)
            capitalized_word = function_value.capitalize()
            return capitalized_word

        return wrapper

    return capitalize_decorator


@capitalize_decorator_with_arguments("the fame", "the fame monster")
def get_my_fav_album_name(album):
    return album

print(get_my_fav_album_name("chromatica"))
