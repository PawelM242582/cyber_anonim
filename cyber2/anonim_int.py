
def anonim_int(data):
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
    anonym.numeric_noise('sttl')
    anonym.numeric_noise('dttl')
    anonym.numeric_noise('swin')
    anonym.numeric_noise('dwin')
    anonym.numeric_noise('stcpb')
    anonym.numeric_noise('dtcpb')
    anonym.numeric_noise('ct_state_ttl')
    anonym.numeric_noise('ct_srv_src')
    anonym.numeric_noise('ct_srv_dst')
    anonym.numeric_noise('ct_dst_ltm')
    anonym.numeric_noise('ct_src_ ltm')
    anonym.numeric_noise('ct_src_dport_ltm')
    anonym.numeric_noise('ct_dst_sport_ltm')
    anonym.numeric_noise('ct_dst_src_ltm')



    anonym = anonym.to_df()

    df['sloss'] = np.abs(anonym['sloss'])
    df['dloss'] = np.abs(anonym['dloss'])
    df['Spkts'] = np.abs(anonym['Spkts'])
    df['Dpkts'] = np.abs(anonym['Dpkts'])
    df['smeansz'] = np.abs(anonym['smeansz'])
    df['dmeansz'] = np.abs(anonym['dmeansz'])
    df['sttl'] = np.abs(anonym['sttl'])
    df['dttl'] = np.abs(anonym['dttl'])
    df['swin'] = np.abs(anonym['swin'])
    df['dwin'] = np.abs(anonym['dwin'])
    df['stcpb'] = np.abs(anonym['stcpb'])
    df['dtcpb'] = np.abs(anonym['dtcpb'])
    df['ct_state_ttl'] = np.abs(anonym['ct_state_ttl'])
    df['ct_srv_src'] = np.abs(anonym['ct_srv_src'])
    df['ct_srv_dst'] = np.abs(anonym['ct_srv_dst'])
    df['ct_dst_ltm'] = np.abs(anonym['ct_dst_ltm'])
    df['ct_src_ ltm'] = np.abs(anonym['ct_src_ ltm'])
    df['ct_src_dport_ltm'] = np.abs(anonym['ct_src_dport_ltm'])
    df['ct_dst_sport_ltm'] = np.abs(anonym['ct_dst_sport_ltm'])
    df['ct_dst_src_ltm'] = np.abs(anonym['ct_dst_src_ltm'])

    return df
