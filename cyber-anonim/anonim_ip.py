def anonimizacion(data,np,pd):
    from anonymizeip import anonymize_ip
    df = data

    a = [anonymize_ip(item, ipv4_mask="0.0.0.255") for item in np.array(df["srcip"])]
    b = [anonymize_ip(item, ipv4_mask="0.0.0.255") for item in np.array(df["dstip"])]

    df['srcip']=a
    df['dstip']=b

    return df