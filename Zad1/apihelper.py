#-*- coding: utf-8 -*-
def info(object, spacing=10, collapse=1):
    u"""Wypisuje metody i ich notki dokumentacyjne.
    Argumentem może być moduł, klasa, lista, słownik, czy też łańcuch znaków."""
    methodList = [e for e in dir(object) if callable(getattr(object, e))]
    processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
    print "\n".join(["%s %s " %
                                    (method.ljust(spacing),
                                     processFunc(unicode(getattr(object, method).__doc__)))
                                    for method in methodList])
if __name__ == "__main__":    #(4) (5)
    print info.__doc__