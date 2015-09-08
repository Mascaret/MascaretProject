# This is a metaclass Singleton
class Singleton(type):
    _instances = {} 
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

#This is the User class, has inherited from a metaclass "type"
class User(metaclass=Singleton):

    def __init__(self,login):
            self.login = login
