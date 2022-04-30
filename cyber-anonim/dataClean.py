
def dataCleaning(data):
    import pandas as pd
    nalist= data.columns[data.isna().any()].tolist()
    typelist = data.dtypes

    for item,typeitem in zip(nalist,typelist):
        if typeitem in ('int64','float64'):
            data[item] = data[item].fillna(0)
        else:
            data[item] = data[item].fillna('Lack')
    return data