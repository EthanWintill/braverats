from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_session import Session
#FLASK TOOLS
from flask_socketio import SocketIO, send, emit
#FLASK SOCKETIO
from games import createNewGame, findGame, socketIdsInGame
#GAMES STORAGE


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


def sendGameState(gid):
    game = findGame(gid)
    sockets = socketIdsInGame(gid)
    for socket in sockets:
        socketio.emit("gstate", {"state":game.printGameState()}, room=socket)
    

@socketio.on('message')
def handleMessage(cardNum):
    if(games.games[gameID].applewood_id==request.sid): #senders team should be taken from client data eventually, but this will do for not
        sender = 'applewood'
        global waitingOnApplewood
        waitingOnApplewood = False
        global appPickedcard 
        appPickedcard = cardNum
    else:
        sender = 'yarg'
        global waitingOnYarg 
        waitingOnYarg = False
        global yargPickedcard
        yargPickedcard = cardNum
    
    if(not waitingOnApplewood and not waitingOnYarg):
        games.games[gameID].chooseCards(int(appPickedcard),int(yargPickedcard))
        games.games[gameID].calculate()
        waitingOnApplewood = True
        waitingOnYarg = True
        emit("played",{"cardValue":yargPickedcard, 'result':games.games[gameID].printGameState()}, room = games.games[gameID].applewood_id)
        emit("played",{"cardValue":appPickedcard, 'result':games.games[gameID].printGameState()}, room = games.games[gameID].yarg_id)

    

@socketio.on('connect')
def handleConnect():
    pass
        
    
    


if __name__ == '__main__':
    socketio.run(app, port=3000, debug=True)
    
 
 