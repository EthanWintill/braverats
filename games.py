from braverats import Game
import random
import string
import hashlib

games = {}


CHARACTERS = (
    string.ascii_letters
    + string.digits
)

def generate_unique_key():
    return ''.join(random.sample(CHARACTERS, 15))

def createNewGame(oldGID = None):
    global games
    if len(games) > 4:
        games = {}
    if oldGID is None: #check if new match instead of rematch
        gId = generate_unique_key()
        ng = Game(gId)
        games[gId] = ng
        return gId

    #if we're at this point we know it's rematch
    gId = hashlib.md5(oldGID.encode()).hexdigest()[:15] #generate pseudorandom id from old id
    try: 
        findGame(gId) #check if game has already been created (client is second to click rematch)
    except:
        ng = Game(gId) #create new game if client was the first to click rematch
        games[gId] = ng
    return gId

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
    return ids






