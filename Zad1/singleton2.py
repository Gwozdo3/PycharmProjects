#-*- coding: utf-8 -*-
#nazwa klasy i dziedziczenie z bazowej klasy object
class MySingleton(object):

    #ustawienie zmiennej instance na Null
    _cokolwiek=None
    #przy pierwszym wywolaniu klasy _instance zostanie ustawione na wskaznik
    #pierwszego MySingletona i kazdy kolejny stworzony obiekt
    #bedzie odwolywal sie do pierwszego

    #definicja __inita__ z parametrem self (konstruktora)
    def __new__(self):

        #if ponizszy sprawdza czy została wczesniej stworzona instancja MySingletona
        #jeżeli nie została to tworzy ją i zwraca, jeżeli została wczesniej stworzona,
        #to poprostu odwołuje się do pierwszej
        if not self._cokolwiek:
            self._cokolwiek=super(MySingleton,self).__new__(self)

            #KODZIK WYKONYWALNY NP ZMIENNE ITP.
            self.y=10

            #
        return self._cokolwiek

z=MySingleton()
x=MySingleton()
x.y=20

print z.y #wypisze 20
