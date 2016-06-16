class MySingleton(object):
    _instance=None
    def __new__(self):
        if not self._instance:
            self._instance=super(MySingleton,self).__new__(self)
            #KODZIK WYKONYWALNY NP ZMIENNE ITP.
            self.y=10


            #
        return self._instance

x=MySingleton()
x.y=20
z=MySingleton()
print z.y
