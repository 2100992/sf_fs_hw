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
    Находит все альбомы в базе данных по заданному артисту
    """
    session = connect_db(DB_PATH)
    artists = session.query(Album).all()
    result = []
    for artist in artists:
        if artist.artist not in result:
            result.append(artist.artist)
    return result

def save_album(album_info):
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