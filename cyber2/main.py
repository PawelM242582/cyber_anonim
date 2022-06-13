from datareader import dataread
from dataClean import dataCleaning
from anonim_ip import anonimizacion
from anonim_int import anonim_int
from anonim_ports import anonim_ports
from anonim_timestamps import anonim_timestamps

filename = r'UNSW-NB15_4'

data = dataread(filename)
data = dataCleaning(data)
data = anonimizacion(data)
data = anonim_int(data)
data = anonim_ports(data)
data = anonim_timestamps(data)

data.to_csv('dane/' + filename+'_anonymized_new.csv', index=False)
