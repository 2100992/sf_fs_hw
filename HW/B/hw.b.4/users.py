import uuid
from datetime import datetime as dt

import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_PATH = 'sqlite:///sochi_athletes.sqlite3'
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = sa.Column(sa.Integer, primary_key=True)
    first_name = sa.Column(sa.Text)
    last_name = sa.Column(sa.Text)
    gender = sa.Column(sa.Text)
    email = sa.Column(sa.Text)
    birthdate = sa.Column(sa.DATETIME)
    height = sa.Column(sa.REAL)


def connect_db(DB_PATH):
    engine = sa.create_engine(DB_PATH)
    Base.metadata.create_all(engine)
    session = sessionmaker(engine)
    return session()

def valid_email(email):
    from re import compile, match

    pattern = compile(r'(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)')

    return match(pattern, email)

def valid_height(height, gender):
    try:
        height = float(height)
    except:
        return False
    if height in range(0,50) and gender == 'м':
        print('Рост!')
        return False
    elif height not in range (100, 260):
        return False
    return True

def valid_birthdate(day):
    try:
        day = dt.strptime(day, "%d/%m/%Y" )
    except:
        print('Неправильный формат даты. Укажите дату своего рождения в формате дд/мм/ггг: ')
        return False
    delta = (dt.today() - day)
    age = int(delta.days/365)
    if age not in range (14, 110):
        print(f'Что-то не верится, что вам {age} лет')
        return False
    return day

def request_data():
    print('Регистрация пользователя!')
    name = input('Укажите своё имя: ')
    last_name = input('Укажите фамилию: ')

    gender = input('Укажите свой пол: ')
    while gender not in {'м','М','ж','Ж','мужчина','Мужчина','женщина','женщина'}:
        gender = input('Вы серьездно? Укажите свой настоящий пол: ')
    gender = 'м' if gender in {'м','М','мужчина','Мужчина'} else 'ж'

    email = input('Укажите свой адрес электронной почты: ')
    while not valid_email(email):
        email = input('Укажите корректный адрес электронной почты: ')
    
    birthdate = ''
    while not isinstance(birthdate, dt):
        birthdate = input('Укажите дату своего рождения в формате дд/мм/ггг: ')
        birthdate = valid_birthdate(birthdate)

    height = input('И последнее. Укажите свой рост в сантиметрах: ')
    while not valid_height(height, gender):
        height = input('Укажите свой рост в сантиметрах: ')
    height = float(height)

    user = User(
        first_name=name,
        last_name=last_name,
        gender = gender,
        email=email,
        birthdate = birthdate,
        height = height
        )

    return user

def main():
    session = connect_db(DB_PATH)
    one_more = True
    while one_more:
        user = request_data()
        session.add(user)
        session.commit()
        print("Спасибо, данные сохранены!")
        answer = input('Хотите добавить еще одного пользователя? ')
        one_more = True if answer in {'y', 'Y','yes','Yes','да','Да','YES','Да','может быть','наверное'} else False

if __name__ == "__main__":
    main()