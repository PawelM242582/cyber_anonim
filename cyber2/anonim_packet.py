
def anonim_packet(data):
    import pandas as pd
    import numpy as np
    from anonympy.pandas import dfAnonymizer

    df = data
    anonym = dfAnonymizer(df)
    anonym.numeric_noise('sloss')
    anonym.numeric_noise('dloss')
    anonym.numeric_noise('Spkts')
    anonym.numeric_noise('Dpkts')
    anonym.numeric_noise('smeansz')
    anonym.numeric_noise('dmeansz')

    anonym = anonym.to_df()

    df['sloss'] = np.abs(anonym['sloss'])
    df['dloss'] = np.abs(anonym['dloss'])
    df['Spkts'] = np.abs(anonym['Spkts'])
    df['Dpkts'] = np.abs(anonym['Dpkts'])
    df['smeansz'] = np.abs(anonym['smeansz'])
    df['dmeansz'] = np.abs(anonym['dmeansz'])

    return df
