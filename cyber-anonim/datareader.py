
def dataread(pd):
    try:
        path = r'cyber\UNSW_NB15\UNSW-NB15_1.csv'
        label = r'cyber\UNSW_NB15\NUSW-NB15_features.csv'
        ng = pd.read_csv(label,low_memory=False,encoding_errors='ignore')
        df = pd.read_csv(path,names=ng['Name'],low_memory=False,encoding_errors='ignore')
        return df
    except FileNotFoundError as NoSuchFile:
        print(NoSuchFile)
    except Exception as e:
        print(e)
