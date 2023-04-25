from sqlalchemy import create_engine, Column, Integer, String, select, update, delete, func
#from sqlalchemy.sql import func
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
    
    @staticmethod
    def getLeaderboard():
        query = (
            session.query(
                User.id,
                User.username,
                func.sum(func.cast(Game.applescore == 4, Integer)),
                func.sum(func.cast(Game.yargscore == 4, Integer)),
                func.count(Game.id).label('games_played')
            )
            .outerjoin(Game, (User.id == Game.appleid) | (User.id == Game.yargid))
            .group_by(User.id)
        )

        leaderboard = []
        for user_id, username, appwins, yargwins, games_played in query:
            #win_loss_ratio = wins / losses if losses > 0 else wins
            leaderboard.append({
                'id': user_id,
                'username': username,
                'games_played': games_played,
                'wins': appwins,
                'yargwins': yargwins
                # 'losses': losses,
                # 'win_loss_ratio': win_loss_ratio
            })

        return leaderboard
