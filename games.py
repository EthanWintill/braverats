from braverats import Game
import random
import string


games = {}


CHARACTERS = (
    string.ascii_letters
    + string.digits
)

def generate_unique_key():
    return ''.join(random.sample(CHARACTERS, 15))

def createNewGame():
    gId = generate_unique_key()
    ng = Game(gId)
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






