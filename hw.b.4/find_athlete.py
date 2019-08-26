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

def find_user(session, first_name = None, last_name = None, id = None):
    if isinstance(id, int):
        query = session.query(User).filter(User.id == id)
        if query.count():
            return query.first
    if first_name and last_name:
        query = session.query(User).filter(User.first_name and last_name)
        if query.count():
            return query.first
    elif first_name:
        query = session.query(User).filter(User.first_name)
        if query.count():
            return query.first
    elif last_name:
        query = session.query(User).filter(User.last_name)
        if query.count():
            return query.first
    print('Такой пользователь не найден')
    return None

#Найдем ближайшего спортсмена по росту
#Делаем два запроса:
#   -забираем всех кто ниже, сортируем от большего к меньшему, забираем первого
#   -берем всех, кто выше, сортируем от меньшего к большему, забираем первого
#   сравниваем
def find_nearest_height(session, height):
    athlete1 = session.query(Athlete).filter(Athlete.height <= height).order_by(Athlete.height.desc()).first()
    athlete2 = session.query(Athlete).filter(Athlete.height >= height).order_by(Athlete.height.asc()).first()
    if abs(athlete1.height - height) < abs(athlete2.height - height):
        return athlete1
    return athlete2


#для тестов
def print_query(query):
    for record in query:
        print(record)


def main():
    session = connect_db(DB_PATH)

    print('Давайте найдем в по базе похожих спортсменов.')
    first_name = input('Укажите пользователя: ')
    last_name = input('Укажите фамилию искомого спорстмена: ')
    
    desired_users = find_user(first_name, last_name, session)
    print(f'{desired_users[0][first_name]} {desired_users[0][last_name]}. Возраст - {desired_users[0][age]}. Рост - {desired_users[0][height]}')
    print(f'{desired_users[1][first_name]} {desired_users[1][last_name]}. Возраст - {desired_users[1][age]}. Рост - {desired_users[1][height]}')
    print(f'{desired_users[2][first_name]} {desired_users[2][last_name]}. Возраст - {desired_users[2][age]}. Рост - {desired_users[2][height]}')

if __name__ == "__main__":
    main()
