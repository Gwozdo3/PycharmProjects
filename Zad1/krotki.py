# krotki to niezmienne listy (nie da sie edytowac w zaden sposob)
# okreslane nawiasami zwyklymi ()()()()()()()()()()
t = ("a", "b", "mpilgrim", "z", "element")
print t
print t[1:3]
# KROTKI NIE MAJO METOD TYPU .index() czy .append()
# krotki nie tak jak listy moga byc uzywane jako klucze w dictach!!
print "---------------------------"
list = list(t) #zamiana krotki na liste

print list
list.append("cosik") # dopisanie cosiku na koniec listy
print "---------------------------"
krot= tuple(list) #zamiana listy na krote
print krot
