
class Single(object):

    _instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Single.__instance == None:
            Single()
        return Single.__instance

    def _init_(self):
        """ Virtually private constructor. """
        if Single.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Single.__instance = self

