from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_session import Session
#FLASK TOOLS
from flask_socketio import SocketIO, send, emit
#FLASK SOCKETIO
from games import createNewGame, findGame, socketIdsInGame
#GAMES STORAGE
import json


#from forms import AddTaskForm, CreateUserForm, LoginForm
#from database import Tasks, Users
#from flask_login import LoginManager, login_user, logout_user, login_required, current_user
#from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

socketio = SocketIO(app, cors_allowed_origins="*")


@app.route("/play/<string:gId>")
def play(gId):
    try:
        findGame(gId)
    except:
        return "GAME NOT FOUND"
    
    session['gid'] = gId
    game = findGame(gId)
    if not game.playersIn() and not game.sidToTeam(session.sid):
        game.assignPlayer(session.sid)
    
    return render_template("play.html", sid=session.sid)




@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        val = createNewGame()
        return render_template("index.html", gameId=val)
    return render_template("index.html")

@socketio.on("connection")
def assignPlayer(data):
    
    gid = data['gid']
    try:
        game = findGame(gid)
    except:
        return
    sid = data['sid']
    print("SID " + sid)
    game.assignSocket(sid,request.sid) # handles wrong users in func
    sendGameState(gid)


def sendGameState(gid, round_winner=None):
    game = findGame(gid)
    sockets = socketIdsInGame(gid)
    dataForClient = {
            'applewood_hand': game.applewood.hand,
            'yarg_hand':game.yarg.hand,
            'applewood_score':game.applewood.score,
            'yarg_score':game.yarg.score,
            'applewood_card':game.applewood.card,
            'yard_card':game.yarg.card,
            'gameover':game.gameOver(), #winner is set to applewood, or yarg if they win, none if game isn't over, and tie if they tie
            'game_winner':('tie' if game.gameOver() else 'none' ) if not game.winner else ('apple' if game.winner==1 else 'yarg'),
            'round_winner': round_winner
        }
    for socket in sockets:
        socketio.emit("gstate", {"state":dataForClient,"team":game.sidToTeam(socket)}, room=socket)
    

@socketio.on('playedCard')
def handleMessage(data):
    try:
        game = findGame(data['gid'])
    except:
        print("game not found dumb TY")
        return
    sid = data['sid']
 #fix this 
    if(game.applewood.sessionid==sid): 
        game.chooseApplewood(int(data['card']))
    elif(game.yarg.sessionid==sid):
        game.chooseYarg(int(data['card']))
    else:
        print("you're a spectatr AR")
    
    if(game.applewood.card and game.yarg.card):
        roundWinner = game.calculate()
        sendGameState(data['gid'], roundWinner)

    

@socketio.on('connect')
def handleConnect():
    pass
        
    
    


if __name__ == '__main__':
    socketio.run(app, port=3000, debug=True)
    
 
 