def anonim_timestamps(data):
    import pandas as pd

    df = data
    df = pd.DataFrame(df)
    df.drop('Stime', inplace=True, axis=1)
    df.drop('Ltime', inplace=True, axis=1)

    return df
