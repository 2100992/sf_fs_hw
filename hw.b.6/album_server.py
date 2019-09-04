from bottle import route
from bottle import run
from bottle import HTTPError

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
def albums(artist):
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


if __name__ == "__main__":
    run(host="localhost", port=8080, debug=False)