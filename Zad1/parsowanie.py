#-*- coding: utf-8 -*-
k = "uid"
v = "sa"
print "%s=%s" % (k, v) # %s oznacza ze w jego miejsce wchodzi kolejna zmienna z nawiasu
#reszta znakow bez zmian
#(k,v) to tupel!!

userCount = 6
print "Uzytkownikow: %d" % (userCount, ) #uzywamy tego np podczas gdy chcemy do stringa
#dodac przy wypisaniu wartosc cyfrową

#print "Uzytkownikow: " + userCount   --- nie zadziala
print "Dzisiejsza cena akcji: %.2f" % 50.4625 # %f jak float .2 jak 2 po przecinku
print "Zmiana w stosunku do dnia wczorajszego: %+.2f" % 1.5333 #+ jak dodanie znaku plusa