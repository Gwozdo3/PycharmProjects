class Singleton:
    #private class can't be accessed by user so all methods are are being put into private Singleton class
    class __Singleton:
        def __init__(self, arg):
            self.val = arg
        def __str__(self):
            return repr(self) + self.val
    #During initialisation checks if instance is None if not it uses __Singleton if it is
    # it creates initialises private singleton
    instance = None
    def __init__(self, arg):
        if not Singleton.instance:
            Singleton.instance = Singleton.__Singleton(arg)
        else:
            Singleton.instance.val = arg
    def __getattr__(self, name):
        return getattr(self.instance, name)


if __name__ == "__main__":
    a = Singleton('aaa')
    print a
    b = Singleton('bbb')
    c = Singleton('ccc')
    print a
    print b
    print c
    #all instances of Singleton are the same