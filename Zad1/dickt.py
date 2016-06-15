#W KLAMRACH WARTOSCI {}{}{{{}}{}{}{}{}{}{}{{}!!!!
# kluczami nie moga byc elementy zmienne np listy
a="server"
d = {a:"mpilgrim", "database":"master"}   #utworzenie dict
print d                                          #wpisanie dicta

print "---------------"
print d["server"]                       #wypis wartosci przypisanej do klucza server

print d["database"]                     # same

d["uid"] = "sa"                         #dodanie klucza z przyp. wartoscia to dicta
d["licznik"] = 3                    # same ale z innym typem danej (dziala okej)
d[42] = "douglas"                   #same ale z innym typem klucza

print d                                         #wpisanie dicta
print d[42]                                     #same i dziala
del d[42]                                   #del klucza i wartosci
print d
d.clear()                                       #wyczyszczenie dicta
print d