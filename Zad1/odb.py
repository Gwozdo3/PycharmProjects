import odbchelper
params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
print odbchelper.buildConnectionString(params)
print odbchelper.buildConnectionString.__doc__