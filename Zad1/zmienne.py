if __name__ == "__main__":
    myParams = {"server":"mpilgrim", \
    "database":"master", \
    "uid":"sa", \
    "pwd":"secret" \
    }
    # backslash pozwala na dokonczenie czegos w next linii a Pajton nie bd patrzyl na wciecie
print myParams

v = ("a","b","c")
# do v wpisujemy 3 lememntowego tupla
print v
(d,e,f) = v
#do zmiennych d,e,f przypisujemy kolejne elementy tupla v
#wazne ze ilosc zmiennych musi byc taka sama jak ilosc elementow w tuplu (tutaj 3)
print d
print e
print f

#some thingz

print "--------------------\
----------------" #kekeszky

indeksy = range(3) #lista
#range 3 zwraca kolejne wartosci od zera (tutaj 0,1,2)
print indeksy
print "--------------------"
lista=["a","b","c","d","e","f"]
x=len(lista)

#ponizej maly for przeskakujacy przez wszystkie elementy listy
for cokolwiek in range(x):
    i=cokolwiek
    print lista[i]

#cosik (przypisanie wartosci dniom tygodnia)
(PONIEDZIALEK, WTOREK, SRODA, CZWARTEK, PIATEK, SOBOTA, NIEDZIELA) = range(7)
print SRODA
#end