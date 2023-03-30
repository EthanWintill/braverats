from flask import Flask, render_template, request, redirect, url_for, flash
import games as games
from flask_socketio import SocketIO, send, emit
from braverats import Game
#from forms import AddTaskForm, CreateUserForm, LoginForm
#from database import Tasks, Users
#from flask_login import LoginManager, login_user, logout_user, login_required, current_user
#from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/play/<int:gId>")
def play(gId):
    try: 
        g = games.games[gId]
    except:
        return "GAME NO EXISTO"
    return render_template("play.html")

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        val = games.curInc
        games.games[games.curInc] = Game()
        games.curInc += 1
        return render_template("index.html", gameId=val)
    return render_template("index.html")


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
    print(f"it worked! Game: {games.curInc}")
    if(games.games[gameID].yarg_id is None):
        print("\n\n\n\nsetting yarg_id to this player: "+request.sid)
        games.games[gameID].yarg_id = request.sid
    elif(games.games[gameID].applewood_id is None):
        print("\n\n\n\nsetting applewood id to this player: "+request.sid)
        games.games[gameID].applewood_id = request.sid


gameID = 0 #need to fix these to generalize to multiple games
waitingOnApplewood = True
waitingOnYarg = True
appPickedcard = -1
yargPickedcard = -1
if __name__ == '__main__':
    socketio.run(app)
 
 