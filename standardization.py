from sklearn.preprocessing import StandardScaler

def std_scaler(data):
    """ 
    引数 data に対し、標準化を行う。

    args:
        list data; 何らかの特徴ベクトルのデータセット

    return:
        list data_std; 標準化された特徴ベクトル
     """
    scaler = StandardScaler()
    scaler.fit(data)
    # "transform"で標準化された値を取得. 
    data_std=scaler.transform(data)


    return data_std