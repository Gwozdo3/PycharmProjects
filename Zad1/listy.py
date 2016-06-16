#W [][][][][][][][][][][][][] WARTOSCI!!!!
#-*- coding: utf-8 -*-
li = [ "a", "b", "mpilgrim", "z", "przykład"]  #dekl listy z kolejno podanymi argumentami
print li #wypis calej listy
print li[2] #wypis konk elementu
print li[-1] # wypis 1 elementu od konca
print li[2:-1] # wypis elementow od indeksu a wlacznie  do b (bez elementu b)
print "---------------------------------------------"
print li[2] # dla testu
print li[:2] # to samo tylko ze od poczatku do wybranego indeksu NIE WLACZNIE
print li[2:] # to samo tylko od indeksu do konca
print "----------------------------------"

# czyli li[:2] zwroci 2 elementy CZYLI wszystkie elementy PRZED tym z indeksem 2
print "-------------------------------------"
li.append("nowy") # dodaje element na koncu tablicy (1 element)
print li
print "---------------------------------------------"
li.insert(2,"nowy") # dodaje element w okreslone indeksem miejsce tablicy (1 element)
# reszte przesuwa o 1 w lewo
print li
print "---------------------------------------------"

li2 = [ "dwa", "elementy","cos1", "cos2"]
li.extend(li2[:2]) # dodaje  wskazane elementy li[0,1]  listy(li2) na koniec listy(li)
print li
print "---------------------------------------------"
li.append(["cos1","cos2"])  # dodaje 2 elementy na koncu tablicy (jako 1 element!!)
#czyli jak sie odwolamy do tego co oddalismy przez indeks -1
# to otrzymamy liste nie jedem element
print li
print "---------------------------------------------"

#CZYLI EXTENDUJEMY JAK CHCEMY DODAC ELEMENTY
# A APPENDUJEMY JAK CHCEMY DODAC TYP np. INNA LISTE

print li.index("dwa") # WYSWIETLA index wybranego elementu z tablicy
# w przypadku powtorzen elementow zawsze wypisze index pierwszego

#jezeli w liscie li znajduje sie element "dwa" to zwroci true i wykona to co nizej
if "dwa" in li  :
    print "jest"
else:
    print "nima"

print"----------------------------------------"
li.remove("dwa") # usuwa wartosc "dwa" z listy
print li
li.remove(li[3]) # usuwa 4 element listy (indeks 3)
print li
print li.pop() #usuwa ostatni element listy i zwraca jego wartosc
print li

print "-----------------------"
print "operatory"
#operatory i ich dzialanie
print li + ["koteczek","2"] # tu tylko wypisze jak lsta by wygladala
print li
print "-----------------------"
li += ["koteczek","2"] # dodaje elementy na koniec tablicy (jak extend)
print li
li = li*2 # mnozy tablice *2 (dodaje 2 razy taka sama tablice do siebie)
print li


print "==================================================="

# dzialania na listach (odwzorowywanie)
li3 = [1, 9, 8, 4]
li3=[element*2 for element in li3] #operacja mnozenia na kazdym elemencie listy
print li3

#teraz pokaz magii:
params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
print params.items() # jak mamy dictionary i wykonamy na nim metode items()
#otrzymamy liste tupli... BENG

## .keys() i .values() zwraca listy kluczy i wartosci, obv

#Metoda values zwraca listę wszystkich wartości. Lista ta jest zgodna z porząd
#kiem listy zwracanej przez metodę keys

params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
print ["%s=%s" % (k, v) for k, v in params.items()] #takie cus zwroci nam liste
#widac jaką  gdzie k i v są kolejnymi itemami z dicta

#Laczenie elementow powyzszej listy, gdzie kazdy element oddzielimy znakiem ";"
k= ";".join(["%s=%s" % (k, v) for k, v in params.items()])
print k
# tak laczyc mozna tylko elementy typu znakowego (liczba wyrzuci exception)

#metoda split w przypadku stringa rozdziela go na czesci w miejscu wystapienia znaku
#z nawiasa, i zapisuje wynik w tablicy
lisplit1= k.split(";")
print lisplit1 #['pwd=secret', 'database=master', 'uid=sa', 'server=mpilgrim']
#w splicie moga byc 2 argumenty , gdzie drugi definiuje ile max razy ma podzielic:
lisplit2=k.split(";",1)
print lisplit2 #['pwd=secret', 'database=master;uid=sa;server=mpilgrim']



print"------- Filtracja Listy --------------"

li=["a", "mpilgrim", "foo", "b", "c", "b", "d", "d"]
print [randname for randname in li if len(randname) > 1]
#filtruje liste nastepujaco: zwraca element(randname) dla: kazdego elementu (randname) z listy(li) jeżeli
#dlugosc elementu jest > od 1
print [randname+":   posiada w sobie i "for randname in li if ("i") in randname]
#ta sama zasada ale wypisuje element jezeli znajdzie w elemencie listy litere i

dict={"a":"b", "d":"c","z":"f","c":"h"}

print["%s i %s" % (k,v) for k,v in dict.items() if "c" in k or "b" in v ]

#tutaj mamy zabawe z dictionary.
#print wypisuje nam ekran "%k  i  %v" dla każdej pary k i v z dictionary(szuka w .items()) jezeli k=c albo v=b



