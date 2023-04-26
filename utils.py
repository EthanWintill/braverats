from models import Users, History

class Authentic():
    def gen_usr_token(uid, pswd_hash):
        return str(uid) + ' ' + pswd_hash
    def validate_usr_token(token):
        values = token.split(' ')
        user = Users.getUserById(values[0])
        if user and user.password == values[1]:
            #valid
            return True
        return False
    def token_to_id(token):
        return token.split(' ')[0]


def test():
    uid = 3
    hash = 'sha4208539y4395340285u843rhtwreg9g943w89545==='
    token = Authentic.gen_usr_token(uid,hash)
    print(Authentic.token_to_id(token))


def getLeaderboard():
    games = History.readAll()
    users = Users.getAllUsers()
    board = []
    for user in users:
        username = user['username']
        id = user['id']
        wins = 0
        losses = 0
        for game in games:
            if game['appleid'] == id and game['applescore']==4 or game['yargid']==id and game['yargscore']==4:
                wins+=1
            elif game['appleid'] == id and game['applescore']!=4 or game['yargid']==id and game['yargscore']!=4:
                losses+=1
        games_played = wins+losses
        raw_ratio = wins/(wins+losses) if losses>0 or wins>0 else -1
        ratio = int(raw_ratio*100)
        board.append([username,id,games_played,wins,losses,ratio])

    return sorted(board, key=lambda x: x[5], reverse=True)

def userStats(uid):
    stats = {}
    user = Users.getUserById(uid)
    if not user:
        return None
    games = History.filter_by_user_id(uid)
    stats['userinfo']=user.__dict__
    wins = 0
    losses = 0
    game_history = []
    for game in games:
        if game['appleid'] == uid:
            userteam = 'applewood'
            oppteam = 'yarg'
            score = game['applescore']
            oppscore = game['yargscore']
            opp = Users.getUserById(game['yargid'])
            if opp:
                oppname = opp.__dict__['username']
            else:
                oppname = 'Guest'
        else:
            userteam = 'yarg'
            oppteam = 'applewood'
            score = game['yargscore']
            oppscore = game['applescore']
            opp = Users.getUserById(game['appleid'])
            if opp:
                oppname = opp.__dict__['username']
            else:
                oppname = 'Guest'
            
        if game['appleid'] == uid and game['applescore']==4 or game['yargid']==uid and game['yargscore']==4:
            wins+=1
        elif game['appleid'] == uid and game['applescore']!=4 or game['yargid']==uid and game['yargscore']!=4:
            losses+=1
        game_history.append({'user_team_name': userteam, 'score': score, 'opponent_team_name': oppteam, 'opponent_score':oppscore, 'opponent_username':oppname})
    stats['games_played'] = wins+losses
    raw_ratio = wins/(wins+losses) if losses>0 or wins>0 else -1
    stats['ratio'] = int(raw_ratio*100)
    stats['losses'] = losses
    stats['wins']= wins
    stats['game_history'] = game_history

    return stats


