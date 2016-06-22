#nazwa(co dziedziczy po przecinkach)
class FileInfo(dict):
    # notka dokumentacyjna
    u"przechowuje metadane pliku"

    #pola
     x=12


    #metoda __init__ jest pseudo konstruktorem. self to referencja do obecnej instancji klasy(zawsze jest)
    def __init__(self, filename=None):
        pass

c=FileInfo()
print c.x