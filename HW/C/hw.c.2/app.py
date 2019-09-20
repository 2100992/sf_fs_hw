from bottle import route
from bottle import post                     #нужно для отработки POST запросов, но можно и обойдисть @route("/", method = 'POST")
from bottle import run
from bottle import HTTPError
from bottle import request                  #request необходим для доступа к параметрам запроса
from bottle import view                     #Необходимо для работы с шаблонами (лежат в папке views)
from bottle import static_file              #объект необходим для работы со статикой (CSS, JS) Пока не пригодилось. Изначально хотел формировать POST через JS
from bottle import redirect                 #объект необходим для редиректа на другую страницу. Использую после записи альбома с редиректом на страницу артиста.

import plugins.album as album               #модуль для связи с БД
from plugins.make_russian import make_russian #для корректного обображения слова "альбомов"

#Корневая страница. Выводим список исполнителей из базы данных
@route("/")
@view('index')                              #используем шаблон index.tpl
def artist():
    return {"artists": album.artists()}     #в шаблон передаем параметр "artists"

#объект необходим для работы со статикой (CSS, JS) Пока не пригодилось. Изначально хотел формировать POST через JS
@route("/static/<filename:path>")
def send_static(filename):
    return static_file(filename, root="static")

#страница с формой для заведения нового альбома
@route("/albums")
@view('new_album')                          #используем шаблон new_album.tpl
def new_album():
    pass


#Отобразим количество и список альбомов исполнителя.
##Если такого исполнителя нет, выводим ошибку 404.
@route("/albums/<artist>")
@view('albums_artist')
def albums(artist):
    albums_list = album.find(artist)
    if not albums_list:
        message = "Альбомов {} не найдено".format(artist)
        result = HTTPError(404, message)
    else:
        albums_count = len(albums_list)     #кол-во альбомов у исполнителя
        album_names = [album.album for album in albums_list]
        message = "В нашей базе у {} {}: ".format(artist, make_russian(albums_count))
        result = {'message':message, 'album_names':album_names}
    return result


#обработаем POST запрос на добавление нового альбома
@post('/albums')
def post_album():
    #вычитываем данные из запроса
    album_info = {
        'year': request.forms.get("year"),
        'artist': request.forms.get("artist"),
        'genre': request.forms.get("genre"),
        'album': request.forms.get("album"),
    }

    #примитивная проверка на то, что 'year' - это integer
    try:
        album_info['year'] = int(album_info['year'])
        print(f"album_info['year'] = {album_info['year']}")
    except:
        print(f"!!!album_info['year'] = {album_info['year']}")
        message = 'Неверный формат поля "Год" - {}'.format(album_info['year'])
        result = HTTPError(409, message)
        return result

    #проверка на наличие в базе такого-же альбома у этого исполнителя
    if album.check_album(album_info):
        album.save_album(album_info)
    else:
        message = "Альбом {} группы {} уже есть в базе".format(album_info['album'], album_info['artist'])
        result = HTTPError(409, message) 
        return result

    #в случае успешного добавления даннх альбома происходит редирект на исполнителя
    return redirect('/albums/' + album_info['artist'])


if __name__ == "__main__":
    run(server='gunicorn', host='0.0.0.0', port=8000)

# if __name__ == "__main__":
#     run(host="0.0.0.0", port=8080, debug=True)