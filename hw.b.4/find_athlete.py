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

def find(first_name, last_name, session):
    query = session.query(User).filter(User.first_name=first_name and User.last_name=last_name)
    users_cnt = query.count()
    user

# Идея такая:
# -ищем первого подходящего по фамилии и имени. Берем его id, рос и дату
# -делаем запрос по пользователям с таким-же ростом
#       -Если count() больше нуля, берем первого попавшегося
#           -Иначе делаем запрос по пользователям с меньшим ростом с сортировкой (order_by(height)) и забираем последнего
#           -Делаем запрос по пользователям с большим ростом с сортировкой и забираем первого
#           -Сравниваем этих двух и делаем выводы
# -повторяем по дате.

#Нужна функция def find_neares(session, field, value):


def main():
    session = connect_db(DB_PATH)

    print('Давайте найдем в по базе похожих спортсменов.')
    first_name = input('Укажите имя искомого спорстмена: ')
    last_name = input('Укажите фамилию искомого спорстмена: ')
    
    desired_users = find(first_name, last_name, session)
    print(f'{desired_users[0][first_name]} {desired_users[0][last_name]}. Возраст - {desired_users[0][age]}. Рост - {desired_users[0][height]}')
    print(f'{desired_users[1][first_name]} {desired_users[1][last_name]}. Возраст - {desired_users[1][age]}. Рост - {desired_users[1][height]}')
    print(f'{desired_users[2][first_name]} {desired_users[2][last_name]}. Возраст - {desired_users[2][age]}. Рост - {desired_users[2][height]}')

if __name__ == "__main__":
    main()