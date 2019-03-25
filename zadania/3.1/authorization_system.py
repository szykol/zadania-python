class User:
    def __init__(self, username, password):
        self.username = username
        self.password = self._encrypt_password(password)
        self.is_logged = False

    def _encrypt_password(self, password):
        # TODO: hashowanie hasla 
        return password        

    def check_password(self, password):
        crypted = self._encrypt_password(password)
        return crypted == self.password

class AuthenticException(Exception):
    def __init__(self, username=None, user=None):
        self.username = username
        self.user = user

class IncorrectPassword(AuthenticException): pass
class NotPermittedError(AuthenticException): pass
class UsernameAlreadyExists(AuthenticException): pass
class PasswordTooShort(AuthenticException): pass
class NotLoggedError(AuthenticException): pass
class IncorrectUsername(AuthenticException): pass

class PermissionError(Exception): pass

class Authenticator:
    def __init__(self):
        self.users = {}

    def add_user(self, username, password):
        if username in self.users:
            raise UsernameAlreadyExists
        elif len(password) > 7:
            self.users[username] = User(username, password)
        else:
            raise PasswordTooShort
    
    def login(self, username, password):
        if username in self.users:
            user = self.users[username]
            if user.check_password(password):
                user.is_logged = True
                return True
            else:
                raise IncorrectPassword
        else:
            raise IncorrectUsername
        

    def is_logged_in(self, username):
        if username in self.users:
            return self.users[username].is_logged

class Authorizor:
    def __init__(self, authenticator):
        self.permissions = {}
        self.authenticator = authenticator

    def add_permission(self, permission):
        if permission in self.permissions:
            raise PermissionError
        else:
            self.permissions[permission] = set()

    def permit_user(self, username, permission):
        if username in self.authenticator.users:
            if permission in self.permissions:
                self.permissions[permission].add(username)
            else:
                raise PermissionError
        else:
            raise IncorrectUsername

    def check_permission(self, username, permission):
        if not self.authenticator.is_logged_in(username):
            raise NotLoggedError
        
        if permission not in self.permissions:
            raise PermissionError
        elif username not in self.permissions[permission]:
            raise NotPermittedError

        return True
        
authenticator = Authenticator()
authorizor = Authorizor(authenticator)


        
        

