from flask import Flask, render_template, request, redirect, url_for, flash
from flask_socketio import SocketIO, send, emit
import games as games
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
def handleMessage(msg):
    senderSid = request.sid
    #emit(msg,skip_sid=senderSid)
    send(msg, broadcast=True,)

    

@socketio.on('connect')
def handleConnect():
    print(f"it worked! Game: {games.curInc}")

if __name__ == '__main__':
    socketio.run(app)
 