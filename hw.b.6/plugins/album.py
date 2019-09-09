import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DB_PATH = "sqlite:///albums.sqlite3"
Base = declarative_base()


class Album(Base):
    """
    Описывает структуру таблицы album для хранения записей музыкальной библиотеки
    """

    __tablename__ = "album"

    id = sa.Column(sa.INTEGER, primary_key=True)
    year = sa.Column(sa.INTEGER)
    artist = sa.Column(sa.TEXT)
    genre = sa.Column(sa.TEXT)
    album = sa.Column(sa.TEXT)

def connect_db(DB_PATH):
    """
    Устанавливает соединение к базе данных, создает таблицы, если их еще нет и возвращает объект сессии 
    """
    engine = sa.create_engine(DB_PATH)
    Base.metadata.create_all(engine)
    session = sessionmaker(engine)
    return session()


def find(artist):
    """
    Находит все альбомы в базе данных по заданному артисту
    """
    session = connect_db(DB_PATH)
    albums = session.query(Album).filter(Album.artist == artist).all()
    return albums

def artists():
    """
    Возвращает список артистов из базы
    """
    session = connect_db(DB_PATH)
    artists = session.query(Album).all()
    result = []
    for artist in artists:
        if artist.artist not in result:
            result.append(artist.artist)
    return result

def save_album(album_info):
    """
    Запись альбома в БД
    """
    session = connect_db(DB_PATH)
    album = Album(
        year=album_info['year'],
        artist=album_info['artist'],
        genre=album_info['genre'],
        album=album_info['album']
    )
    session.add(album)
    session.commit()
    pass


def check_album(album_info):
    '''
    Проверка на наличие в базе у данного артиста такого альбома
    '''
    print(f"album_info['artist'] = {album_info['artist']}")
    print(f"album_info['album'] = {album_info['album']}")
    session = connect_db(DB_PATH)
    desired_album = session.query(Album).\
        filter(Album.artist == album_info['artist'], Album.album == album_info['album'])
    dacount = desired_album.count()
    print(f'desired_album.count() = {dacount}')
    if dacount != 0:
        for album in desired_album.all():
            print(f'{album.artist}, {album.album}')
        return False
    return True