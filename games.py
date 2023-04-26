from braverats import Game, Bot
import random
import string
import hashlib
import threading

games = {}


CHARACTERS = (
    string.ascii_letters
    + string.digits
)

def generate_unique_key():
    return ''.join(random.sample(CHARACTERS, 15))

def deleteGame(gId):
    global games
    if gId in games:
        del games[gId]
        print("get that game outa here")

def createNewGame(oldGID = None, isOneplayer=False):
    global games

    if oldGID is None: #check if new match instead of rematch
        gId = generate_unique_key()
        ng = Game(gId, isOneplayer=True) if isOneplayer else Game(gId)
        games[gId] = ng
        #set timer
        timer = threading.Timer(20 * 60, deleteGame, args=[gId])
        timer.start()
        return gId

    #if we're at this point we know it's rematch
    gId = hashlib.md5(oldGID.encode()).hexdigest()[:15] #generate pseudorandom id from old id
    try: 
        findGame(gId) #check if game has already been created (client is second to click rematch)
    except:
        ng = Game(gId, isOneplayer=True) if isOneplayer else Game(gId) #create new game if client was the first to click rematch
        games[gId] = ng
        #timer
        timer = threading.Timer(20 * 60, deleteGame, args=[gId])
        timer.start()
    return gId

def createOnePlayerGame(oldGID = None): #literally exactly the same as before except for the game constuctor
    return createNewGame(oldGID,True)


def findGame(gId) -> Game:
    if not games[gId]:
        return None
    return games[gId]

def socketIdsInGame(gId):
    game = findGame(gId)
    ids = []
    if game.applewood.socketid:
        ids.append(game.applewood.socketid)
    if game.yarg.socketid:
        ids.append(game.yarg.socketid)
    print("SPECS " )
    print(game.spectators)
    for spec in game.spectators:
        if spec.socketid:
            ids.append(spec.socketid)
    return ids








