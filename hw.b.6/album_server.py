import json

from bottle import route
from bottle import run
from bottle import HTTPError
from bottle import request

import album

@route("/albums/<artist>")
def albums(artist):
    albums_list = album.find(artist)
    if not albums_list:
        message = "Альбомов {} не найдено".format(artist)
        result = HTTPError(404, message)
    else:
        album_names = [album.album for album in albums_list]
        result = "Список альбомов {}: ".format(artist)
        result += ", ".join(album_names)
    return result

@route("/album/<artist>")
def albums2(artist):
    albums_list = album.find(artist)
    if not albums_list:
        message = "Альбомов {} не найдено".format(artist)
        result = HTTPError(404, message)
    else:
        album_names = [album.album for album in albums_list]
        result = "Список альбомов {}<br>".format(artist)
        result += "<br>".join(album_names)
    return result

@route("/")
def artist():
    artists_list = album.artists()
    aritst_name = [artist.artist for artist in artists_list]
    result = '<br>'.join(aritst_name)
    return result


def save_user(user_data):
    first_name = user_data["first_name"]
    last_name = user_data["last_name"]
    filename = "{}-{}.json".format(first_name, last_name)

    with open(filename, "w") as fd:
        json.dump(user_data, fd)
    return filename


@route("/user", method="POST")
def user():
    user_data = {
        "first_name": request.forms.get("first_name"),
        "last_name": request.forms.get("last_name"),
        "birthdate": request.forms.get("birthdate")
    }
    resource_path = save_user(user_data)
    print("User saved at: ", resource_path)

    return "Данные успешно сохранены"



if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True)