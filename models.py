from sqlalchemy import create_engine, Column, Integer, String, select, update, delete
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask_login import UserMixin

engine = create_engine('sqlite:///data.db')
Base = declarative_base()

class User(Base, UserMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(50), unique=True)
    username = Column(String(20), unique=True)
    password = Column(String(256), unique=True)

class Game(Base):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True)
    appleid = Column(Integer, default=0)
    yargid = Column(Integer, default=0)
    applescore = Column(Integer)
    yargscore = Column(Integer)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

session = Session() #use to modify database

class Users():
    def getUserById(id):
        usr = session.query(User).get(id)
        return usr
    def getUserByName(name):
        user = session.query(User).filter_by(username=name).first()
        return user
    def createUser(username, email, pswd):
        try:
            usr = User(username=username, email=email, password=pswd)
            session.add(usr)
            session.commit()
            return True
        except:
            session.rollback()
            return False
    def getAllUsers():
        users = session.query(User).all()
        users_as_dict = [user.__dict__ for user in users]
        return users_as_dict
class History():
    def append(aid,yid,ascr,yscr):
        game = Game(appleid=aid,yargid=yid,applescore=ascr,yargscore=yscr)
        session.add(game)
        session.commit()
    def readAll():
        games = session.query(Game).all()
        games_as_dict = [game.__dict__ for game in games]
        return games_as_dict