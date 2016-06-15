
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
print type (odbchelper)
print type(odbchelper) == types.ModuleType
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
print str(list)
print type(str(list))