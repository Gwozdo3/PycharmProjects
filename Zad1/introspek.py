#-*- coding: utf-8 -*-

#dzieki takiemu importowi mozemy sie do metody info odwolac bezposrednio przez nazwe
from apihelper import info
import types
import odbchelper


li = []
#info(li)
#a tutaj ttrzebabylo by napisac odbchelper.metoda()

#info(odbchelper)


#funkcje wbudowane!
print "----- type() -----"
print type (odbchelper) #zwraca typ czegokolwiek (modulu inta str listy whatever)
print type(odbchelper) == types.ModuleType #sprawdza czy typ obdc == Typoowi ModuleType (true/false)
print"-----  str()  -----"
liczba=1
print type (liczba)
liczba=str(liczba)
print type (liczba)
print"-----------"

list=["s","a","v","c"]
print list
print type(list)
print "lista zamieniona na string"
print str(list) #wypisuje liste jako string
print type(str(list)) #sprawdza typ listy zmienionej na string (kek)
print "-----cos--------"
print str(odbchelper)  #cos takiego wyswietli nam sciezke do obdchelpera (modułu)
print"----------------"

#tak samo jak str dziala metoda unicode() tylko zamiast stringa zwraca unikod
print unicode("eździectwo", "utf-8")  # 1 argument to co przekonwertowac a 2gi to jakiego kodowania uzywano przy tworzeniu

#kolejną funkcją jest dir() ktora zwraca atrybuty czegos co podamy w naiwasie np modułu
print dir(odbchelper)

print"-------------------"
#kolejne jest callable(): zwraca true jak mozna wywolac dana funkcje/obiekt itp
import string
print string.punctuation
print string.join
print callable(string.punctuation)
print callable(string.join)

#Wyswietla nam wbudowane funkcje w pajtonie
import __builtin__
info(__builtin__, 20)

print "--------------------------"

print "--------------------------"

print "--------------------------"

print "--------------------------"
#teraz funkcja getattr zwraca referencje do wybranej metody w konk. objekcie

object = odbchelper
method = "buildConnectionString"
print getattr(object,method)
lista = []
print getattr(lista,"append")

print "--------------------------"