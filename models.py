from sqlalchemy import create_engine, Column, Integer, String, desc, or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
class Users(Base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    age = Column(Integer)

engine = create_engine('sqlite:///C:\\Users\\USER\\Desktop\\hw\\db\\users.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

users = [Users(first_name = 'Mikhail', last_name = 'Kovalev', age = '24'),
         Users(first_name = 'Alexey', last_name = 'Filimonov', age = '24'),
         Users(first_name = 'Victor', last_name = 'Yanchenko', age = '52'),
         Users(first_name = 'Maxim', last_name = 'Semenov', age = '23'),
         Users(first_name = 'Oleg', last_name = 'Budko', age = '35')]
for user in users:
    session.add(user)
    session.commit()

top_users = session.query(Users).order_by(desc(Users.age)).limit(3).all()
for user in top_users:
    print(f'''ID: {user.id}
First name: {user.first_name}
Last name: {user.last_name}
Age: {user.age} ''')

# В связи с отсуствием пользователей подходящим плд условия для проверки использовал 
# другие данные, но для корректности в отношении условий задач оставил исходные условия
user_john = session.query(Users).filter_by(first_name = 'John').first()
if user_john:
    print(f'''ID: {user_john.id}
First name: {user_john.first_name}
Last name: {user_john.last_name}
Age: {user_john.age} ''')
else:
    print('User John not found')

users_older_20 = session.query(Users).filter(Users.age > 20, Users.last_name.contains('a')).all()
for user in users_older_20:
    print(f'''ID: {user.id}
First name: {user.first_name}
Last name: {user.last_name}
Age: {user.age} ''')

users_between_10_and_20_or_30 = session.query(Users).filter(or_(Users.age.between(10,20), Users.age == 30)).all()
for user in users_between_10_and_20_or_30:
    print(f'''ID: {user.id}
First name: {user.first_name}
Last name: {user.last_name}
Age: {user.age} ''')
session.close()