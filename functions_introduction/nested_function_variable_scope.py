def get_my_fav_album_name(album):

    def return_my_fav_album_name():
        return album

    return return_my_fav_album_name


fav_album_name = get_my_fav_album_name("Chromatica")
print(fav_album_name())