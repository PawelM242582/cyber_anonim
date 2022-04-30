from datareader import dataread
from dataClean import dataCleaning
import pandas as pd
import numpy as np
from anonim_ip import anonimizacion
data = dataread(pd)
data = dataCleaning(data,pd)
data = anonimizacion(data,np,pd)
print(data)