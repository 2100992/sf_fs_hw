from bottle import route, post
from bottle import run
from bottle import HTTPError
from bottle import request
from bottle import view

import plugins.album as album

@route("/")
@view('index')
def artist():
    return {"artists": album.artists()}

@route("/albums")
@view('new_album')
def new_album():
    pass


@route("/albums/<artist>")
@view('albums_artist')
def albums(artist):
    albums_list = album.find(artist)
    if not albums_list:
        message = "Альбомов {} не найдено".format(artist)
        result = HTTPError(404, message)
    else:
        album_names = [album.album for album in albums_list]
        message = "Список альбомов {}: ".format(artist)
        result = {'message':message, 'album_names':album_names}
    return result


@post('/albums')
def post_album():
    album_info = {
        'year': request.forms.get("year"),
        'artist': request.forms.get("artist"),
        'genre': request.forms.get("genre"),
        'album': request.forms.get("album"),
    }

    try:
        album_info['year'] = int(album_info['year'])
        print(f"album_info['year'] = {album_info['year']}")
    except:
        print(f"!!!album_info['year'] = {album_info['year']}")
        message = 'Неверный формат поля "Год" - {}'.format(album_info['year'])
        result = HTTPError(409, message)
        return result

    if album.check_album(album_info):
        album.save_album(album_info)
    else:
        message = "Альбом {} группы {} уже есть в базе".format(album_info['album'], album_info['artist'])
        result = HTTPError(409, message) 
        return result
    '''
    albums_list = album.find(album_info['artist'])
    album_names = [album.album for album in albums_list]
    message = "Список альбомов {}: ".format(artist)
    result = {'message':message, 'album_names':album_names}
    '''
    return 'Это успех'







'''
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

import json

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

'''

if __name__ == "__main__":
    run(host="0.0.0.0", port=8080, debug=True)