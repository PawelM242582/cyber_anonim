def anonim_ports(data):
    import pandas as pd

    df=data
    df=pd.DataFrame(df)
    df.drop('sport',inplace=True,axis=1)
    df.drop('dsport',inplace=True,axis=1)

    return df
