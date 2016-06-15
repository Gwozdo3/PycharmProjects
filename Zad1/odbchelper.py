#-*- coding: utf-8 -*-
def buildConnectionString(params):
    return ";".join(["%s=%s" % (k, v) for k, v in params.items()])

if __name__ == "__main__":
    asd = {"server":"mpilgrim","database":"master", "uid":"sa","pwd":"secret"}
    print buildConnectionString(asd)



import odbchelper
params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
print odbchelper.buildConnectionString(params)
print odbchelper