#-*- coding: utf-8 -*-

#Logika boolowska:

    #and dziala tak ze zwraca ostatnią wartość True albo pierwszą wartość False
    #{},"",[],0,False,() == False
print 1and 2 and "asd " and {"cs":"ip","kij":"bij"} and (1,2) #wypisze tupla (1,2) bo jest ostatnią wartoscia == True
print 1 and 0 and () and False and 2 #wywali 0 bo jest pierwsza wartoscią == False
print 1 and {} and 2 or  "tekst" or "asda " and "" # wypisze tekst bo z andow wyłoni {} jako False i zOruje z "tekst" i ""
#co w wyniku daje  pierwszą wartosc True czyli "tekst"