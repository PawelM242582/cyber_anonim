from datareader import dataread
from dataClean import dataCleaning
from anonim_ip import anonimizacion
from anonim_packet import anonim_packet

filename = r'UNSW-NB15_1'

data = dataread(filename)
data = dataCleaning(data)
data = anonimizacion(data)
data = anonim_packet(data)

data.to_csv('P_Cyberbezpieczenstwo_w_inzynierii_systemow/dane/' +
            filename+'_anonymized.csv', index=False)
