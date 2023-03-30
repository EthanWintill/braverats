from flask import Flask, render_template, request, redirect, url_for, flash
import games as games
from flask_socketio import SocketIO, send, emit
from braverats import Game
import json
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
    game = games.games[gameID]

    if(game.applewood_id==request.sid): #senders team should be taken from client data eventually, but this will do for not
        sender = 'applewood'
        global waitingOnApplewood
        waitingOnApplewood = False
        game.chooseCard(game.applewood,int(cardNum))
    else:
        sender = 'yarg'
        global waitingOnYarg 
        waitingOnYarg = False
        game.chooseCard(game.yarg,int(cardNum))
    
    if(not waitingOnApplewood and not waitingOnYarg):
        roundWinner = game.calculate()
        waitingOnApplewood = True
        waitingOnYarg = True
        data = {
            'applewood_hand': game.applewood.hand,
            'yarg_hand':game.yarg.hand,
            'applewood_score':game.applewood.score,
            'yarg_score':game.yarg.score,
            'applewood_card':appPickedcard,
            'yard_card':yargPickedcard,
            'gameover':game.gameOver(), #winner is set to applewood, or yarg if they win, none if game isn't over, and tie if they tie
            'game_winner':('tie' if game.gameOver() else 'none' ) if not game.winner else ('apple' if game.winner==1 else 'yarg'),
            'round_winner': roundWinner
        }
        print(json.dumps(data))
        emit("played",{"cardValue":yargPickedcard, 'result':json.dumps(data)}, room = game.applewood_id)
        emit("played",{"cardValue":appPickedcard, 'result':json.dumps(data)}, room = game.yarg_id)

    

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
 
 