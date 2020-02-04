from hashlib import sha256
from getpass import getpass

class password():
   
    def __init__(self):
        self.password = getpass('Password: ')
        self.hash256_pass = sha256(self.password.encode('utf8')).hexdigest()

    def get_hash(self):
        print(self.hash256_pass)
        return (self.hash256_pass)

    def test_with_key(self, hash_key):
        return (self.hash256_pass == hash_key)


def password_test(hash_key=''):
    test = False
    for i in range(5):
        p = password()    
        if (p.test_with_key(hash_key)):
            test=p.test_with_key(hash_key)
            break        

    if not(test):
        print ('Wrong password!!')
        sys.exit()
    return p.password