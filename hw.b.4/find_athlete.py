from datetime import datetime as dt
from time import mktime

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

class Athlete(Base):
    __tablename__ = 'athelete'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.Text)
    gender = sa.Column(sa.Text)
    birthdate = sa.Column(sa.Text)
    age = sa.Column(sa.Integer)
    height = sa.Column(sa.REAL)
    weight = sa.Column(sa.Integer)
    gold_medals = sa.Column(sa.Integer)
    silver_medals = sa.Column(sa.Integer)
    bronze_medals = sa.Column(sa.Integer)
    total_medals = sa.Column(sa.Integer)
    sport = sa.Column(sa.Text)
    country = sa.Column(sa.Text)

def connect_db(DB_PATH):
    engine = sa.create_engine(DB_PATH)
    Base.metadata.create_all(engine)
    session = sessionmaker(engine)
    return session()

'''
Поиск пользователя в таблицу user.
Ищем сначала по id, потом по связке имя/фимилия, потом отдельно по имени или по фамилии.
Возвращаем экземпляр User или None, если юзера не нашли.

Для раскрытия функционала этой функции хорошо бы доделать правильный парсинг одной строки из input, 
а не тупой построчный опрос...
'''
def find_user(session, first_name = '', last_name = '', u_id = ''):
    if isinstance(u_id, int):
        query = session.query(User).filter(User.id == u_id)
        if query.count():
            return query.first()
    if first_name != '' and last_name != '':
        query = session.query(User).filter(User.first_name == first_name and User.last_name == last_name)
        if query.count():
            return query.first()
    elif first_name != '':
        query = session.query(User).filter(User.first_name == first_name)
        if query.count():
            return query.first()
    elif last_name != '':
        query = session.query(User).filter(User.last_name == last_name)
        if query.count():
            return query.first()
    return None

'''
Найдем ближайшего спортсмена по росту
Делаем два запроса:
   -забираем всех кто ниже, сортируем от большего к меньшему, забираем первого
   -берем всех, кто выше, сортируем от меньшего к большему, забираем первого
   сравниваем

На всякий случай цепляем число таких спрортсменов. В дальшейшем можно при выводе указывать это число и
по запросу выводить список с одинаковым ростом.
'''
def find_nearest_height(session, height):
    #Нормализация данных из разных таблиц. В user рост в сантиметрах, в athelete в метрах
    height = height / 100

    athlete1 = session.query(Athlete).filter(Athlete.height <= height).order_by(Athlete.height.desc()).first()
    athlete2 = session.query(Athlete).filter(Athlete.height >= height).order_by(Athlete.height.asc()).first()

    if athlete1 is None:
        athlete = athlete2
    elif athlete2 is None:
        athlete = athlete1
    elif abs(athlete1.height - height) < abs(athlete2.height - height):
        athlete = athlete1
    else:
        athlete = athlete2

    count = session.query(Athlete).filter(Athlete.height == athlete.height).count()
    return {'athlete':athlete, 'count':count}


'''
Найдем ближайшего спортсмена по возрасту

Повторяем предыдущую функцию.
Надо бы их совместить, но пока я не научился передавать аргументы из объявления функции во внутрь типа:
def function(session, field, value):
    x = sesseion.qyery(DBName).fidrer(field <= value).order_by(field.asc()).first()
    .........

С другой стороны - при поиске даты рождения нужно выполнить более другое приведение типов.
'''
def find_nearest_age(session, birthdate):

    #функция формирования struct_time из строки по шаблону.
    st = lambda bd: mktime(dt.strptime(bd, "%Y-%m-%d").timetuple())

    birthdate = birthdate.strftime("%Y-%m-%d")
    athlete1 = session.query(Athlete).filter(Athlete.birthdate <= birthdate).order_by(Athlete.birthdate.desc()).first()
    athlete2 = session.query(Athlete).filter(Athlete.birthdate >= birthdate).order_by(Athlete.birthdate.asc()).first()
    if athlete1 is None:
        athlete = athlete2
    elif athlete2 is None:
        athlete = athlete1
    elif abs(st(athlete1.birthdate) - st(birthdate)) < abs(st(athlete2.birthdate) - st(birthdate)):
        athlete = athlete1
    else:
        athlete = athlete2
    count = session.query(Athlete).filter(Athlete.birthdate == athlete.birthdate).count()
    return {'athlete':athlete, 'count':count}


def main():
    session = connect_db(DB_PATH)

    print('Давайте найдем в по базе похожих спортсменов.')
    print('Укажите то, что знаете о текущем пользователе')
    u_id = input('Если знаете, укажите id пользователя:')
    try:
        u_id = int(u_id)
    except:
        u_id = ''
    first_name = input('Если знаете, укажите пользователя: ')
    last_name = input('Если знаете, укажите фамилию искомого спорстмена: ')
    
    desired_user = find_user(session, first_name, last_name, u_id)
    if desired_user is None:
        print('Такой пользователь не найден')
        return None
    
    print(f'\n{desired_user.first_name} {desired_user.last_name}. День рождения - {desired_user.birthdate.date()}. Рост - {desired_user.height / 100}\n')

    athlete1 = find_nearest_height(session, desired_user.height)['athlete']
    athlete2 = find_nearest_age(session, desired_user.birthdate)['athlete']
    
    print('Ближайший атлет по росту:')
    print(f'{athlete1.name}. День рождения - {athlete1.birthdate}. Рост - {athlete1.height}\n')
    print('Ближайший атлет по возрасту')
    print(f'{athlete2.name}. День рождения - {athlete2.birthdate}. Рост - {athlete2.height}\n')

if __name__ == "__main__":
    main()
