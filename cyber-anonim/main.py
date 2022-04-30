from datareader import dataread
from dataClean import dataCleaning
from anonim_ip import anonimizacion

data = dataread()
data = dataCleaning(data)
data = anonimizacion(data)
print(data)