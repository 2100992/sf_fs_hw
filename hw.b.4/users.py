import uuid

import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_PATH = 'sqlite:///sochi_athletes.sqlite3'
Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = sa.Column(sa.String(36), primary_key = True)
    first_name = sa.Column(sa.text)
    last_name = sa.Column(sa.text)
    gender = sa.Column(sa.text)
    email = sa.Column(sa.text)
    birthday = sa.Column(sa.DATETIME)
    growth = sa.Column(sa.INTEGER)


def connect_db(DB_PATH):
    engine = sa.create_engine(DB_PATH)
    Base.metadata.create_all(engine)
    session = sessionmaker(engine)
    return session()

def valid_email(email):
    """
    Проверяет наличие хотя бы одной точки в домене и знака @ в email. Возвращает True, если email допустимый и False - в противном случае.
    """

    from re import compile, match

    pattern = compile(r'(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)')
    is_valid = match(pattern, email)
    if is_valid:
        return True
    return False

def request_data():
    print('Регистрация пользователя!')
    name = input('Укажите своё имя:')
    last_name = input('Укажите фамилию')
    gender = ''
    while gender not in {'м','М','ж','Ж','мужчина','Мужчина','женщина','женщина'}:
        gender = input('Укажите свой пол')
    gender = 'м' if gender in {'м','М','мужчина','Мужчина'} else 'ж'


def main():
    session = connect_db(DB_PATH)

    
