from models import Users

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

