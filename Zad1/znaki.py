#-*- coding: utf-8 -*-
#wyzej definicja kodowania w utf-8 (dobrze miec zeby wypisywalo polskie znaki)
print ord("a") #konwertuje znak na liczbe
print chr(255) # liczba na znak (range to 0-255)
print "zażółć gęślą jaźń"

#Unikod:
print ord(u"ą") # bez u wywali error bo to znak unicode
print unichr(313) #


#zadanka z unikodem:

errmsg = u"Nie można otworzyć pliku"
print errmsg #Nie można otworzyć pliku
print errmsg.split() #[u'Nie', u'mo\u017cna', u'otworzy\u0107', u'pliku']
print u"Błąd: %s"%errmsg  #Błąd: Nie można otworzyć pliku

print errmsg + u", brak dostępu." #bez u daloby error bo nie mozna dodac unicode do ascii
print u"Błąd: %s"%errmsg # same jak wyzej
#powyzsze nie dizalaja bo uzywa sie polskich znakow i pajton nie ogarnia jakiego
#typu zmienne obrabia(jakby bylo np "Blad: ...") to by przeszlo bo nie ma znakow spec.

#Zmiana kodowania:
cos2=u"asdaąążźżźs"
cos = cos2.encode("utf-8") #encode zwraca nam napis zakodowany w utf8
print cos
print"---"
print cos.decode("utf-8") #decode zwraca nam unikod