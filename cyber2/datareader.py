def dataread(filename):
    import pandas as pd
    try:
        path = r'P_Cyberbezpieczenstwo_w_inzynierii_systemow/dane/'+filename+'.csv'
        label = r'P_Cyberbezpieczenstwo_w_inzynierii_systemow/dane/NUSW-NB15_features.csv'
        ng = pd.read_csv(label, low_memory=False, encoding_errors='ignore')
        df = pd.read_csv(
            path, names=ng['Name'], low_memory=False, encoding_errors='ignore')

        return df
    except FileNotFoundError as NoSuchFile:
        print(NoSuchFile)
    except Exception as e:
        print(e)
