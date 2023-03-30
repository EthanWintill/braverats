import pdb

class Player:
    hand : list[int]
    score : int
    generalLast : bool
    spyLast : bool
    card : int
    id : str

    def __init__(self):
        self.hand = [0,1,2,3,4,5,6,7]
        self.score = 0
        self.generalLast = False
        self.spyLast = False
        self.card = None
        self.applewoodPlayed = False

    def resetEffects(self):
        self.generalLast = False
        self.spyLast = False
        self.card = None

class Result:
    winner : int # 0:TIE, >0:APPLEWOOD, <0:YARG
    aAmbass : bool
    yAmbass : bool
    aGeneral : bool
    yGeneral : bool
    aSpy : bool
    ySpy : bool
    aWin : bool
    yWin : bool

    def __init__(self):
        self.winner = 0 # 0:TIE, >0:APPLEWOOD, <0:YARG
        self.aAmbass = False
        self.yAmbass = False
        self.aGeneral = False
        self.yGeneral = False
        self.aSpy = False
        self.ySpy = False
        self.aWin = False
        self.yWin = False

def battle(a, y): #a:Player(applewood) y:Player(yarg)
    aStrength = a.card + (a.generalLast * 2)
    yStrength = y.card + (y.generalLast * 2)

    wizardInPlay = a.card == 5 or y.card == 5
    result = Result()
    result.aAmbass = a.card == 4 and not wizardInPlay
    result.yAmbass = y.card == 4 and not wizardInPlay
    result.aGeneral = a.card == 6 and not wizardInPlay
    result.yGeneral = y.card == 6 and not wizardInPlay
    result.aSpy = a.card == 2 and not wizardInPlay
    result.ySpy = y.card == 2 and not wizardInPlay
    

    if not wizardInPlay:
        if a.card == 0 or y.card == 0:
            result.winner = 0
        elif a.card == 7 and y.card != 7:
            if y.card == 1:
                win = -1
                result.yWin = True
            else:
                win = 1
        elif y.card == 7 and a.card != 7:
            if a.card == 1:
                win = 1
                result.aWin = True
            else:
                win = -1
        elif a.card == 3 or y.card == 3:
            result.winner = yStrength - aStrength
        else:
            result.winner = aStrength - yStrength
    else:
        result.winner = aStrength - yStrength
    
    return result
            
class Game:
    applewood : Player
    yarg : Player
    curDraws : list[Result]
    maxScore = 4
    winner : int
    yarg_id : str
    applewood_id: str

    def __init__(self):
        self.applewood = Player()
        self.yarg = Player()
        self.curDraws = []
        self.winner = None
        self.yarg_id = None
        self.applewood_id = None

    def chooseCards(self, a, y):
        if a not in self.applewood.hand or y not in self.yarg.hand:
            print("error card not in hand")
            return
        self.applewood.card = a
        self.yarg.card = y
        self.applewood.hand.remove(a)
        self.yarg.hand.remove(y)

    def handleDraws(self, winner): # >0 apple <0 yarg
        for i in range(len(self.curDraws)):
            if winner > 0:
                self.applewood.score += 1
                if self.curDraws[i].aAmbass:
                    self.applewood.score += 1
            else:
                self.yarg.score += 1
                if self.curDraws[i].yAmbass:
                    self.yarg.score += 1
        self.curDraws = []
    
    def calculate(self):
        if not self.applewood or not self.yarg:
            print("cards not chosen before fight")
            return
        result = battle(self.applewood, self.yarg)
        if result.aWin:
            self.applewood.score = self.maxScore
        elif result.yWin:
            self.yarg.score = self.maxScore
        elif result.winner == 0:
            self.curDraws.append(result)
        elif result.winner > 0:
            self.applewood.score += 1
            if result.aAmbass:
                self.applewood.score += 1
            self.handleDraws(1)
        elif result.winner < 0:
            self.yarg.score += 1
            if result.yAmbass:
                self.yarg.score += 1
            self.handleDraws(-1)
        else:
            print("You should not be seeing this")
        
        self.applewood.resetEffects()
        self.yarg.resetEffects()

        self.applewood.generalLast = result.aGeneral
        self.applewood.spyLast = result.aSpy
        self.yarg.generalLast = result.yGeneral
        self.yarg.spyLast = result.ySpy

        self.checkWin()

    def checkWin(self):
        if self.applewood.score >= self.maxScore:
            self.winner = 1
        elif self.yarg.score >= self.maxScore:
            self.winner = -1
        elif len(self.yarg.hand) <= 0 or len(self.applewood.hand) <= 0:
            self.winner = 0

    def gameOver(self):
        if self.winner:
            return True
        else:
            return False
    def printGameState(self):
        result = f"apple: \{self.applewood.hand} \{self.applewood.score}\n\{self.yarg.hand} \{self.yarg.score} \{self.winner}"
        print("apple: ", self.applewood.hand, self.applewood.score)
        print("yarg: ", self.yarg.hand, self.yarg.score)
        print(self.winner)
        return result
        

def testGame():
    game = Game()
    while not game.gameOver():
        inputa = int(input("APPLEWOOD:"))
        inputy = int(input("YARG:"))
       # pdb.set_trace()
        game.chooseCards(inputa,inputy)
        game.calculate()
        game.printGameState()

