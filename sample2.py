import pandas as pd
import matplotlib.pyplot as plt
from standardization import std_scaler
import dataset
import Linear_svc
import plot


def main():
    """ 
    メインプログラム. 全ての特徴に対し、標準化を行う.
     """
    #データセットを作成
    df = dataset.load_dataset()
    
    # 特徴ベクトル名と教師データ名を抽出.
    cols=df.columns

    # 教師データのみ削除
    cols=cols.delete(-1)

    # 標準化の対象となるデータセットを作成.
    df_std=df

    # 全ての特徴ベクトルに対して標準化を行う.
    for col in cols:
        #numpy配列にして、reshapeする.
        data=df[f"{col}"]
        data=data.values.reshape(-1,1)

        #標準化を行う.
        data_std=std_scaler(data)
        df_std[f"{col}"]=data_std

    # 標準化したデータセットに教師データを追加.
    df_std["Class"]=df["Class"]
    

    #出力メッセージをまとめるリスト.
    result_messeges=[]

    # 標準化前のデータセットをロード.
    default = dataset.load_dataset()

    # 標準化前のデータセットで学習.
    result_messeges.append(Linear_svc.fit_k_folds(default))
    
    # 標準化した値に変更し、LinearSVCモデルで実行する.
    result_messeges.append(Linear_svc.fit_k_folds(df_std))


    for i, r in enumerate(result_messeges[0]):
        print(f"default: \n{r}\nstandardization: \n{result_messeges[1][i]}\n")


if __name__=="__main__":
    main()

