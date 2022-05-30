import pandas as pd
import matplotlib.pyplot as plt
from standardization import std_scaler
import dataset
import Linear_svc
import plot


def main():
    """ 
    メインプログラム. ある特定の特徴のみを標準化.
     """
    #データセットを作成
    df = dataset.load_dataset()
    #特定の特徴ベクトルを抜き出す.
    data=df["Area"]
    #numpy配列にして、reshapeする.
    data=data.values.reshape(-1,1)

    #dataの標準化を行う.
    data_std=std_scaler(data)

    #tempに標準化前・後のデータを格納.
    temp=pd.DataFrame(data=data, columns=["Area"])
    temp["standardization"]=data_std

    #二つのデータを可視化
    plot.plot(temp)

    #出力メッセージをまとめるリスト.
    result_messeges=[]

    # レポート1のLinearSVCモデルで標準化前のデータセットを学習する.
    result_messeges.append(Linear_svc.fit_k_folds(df))

    # 標準化した値に変更し、LinearSVCモデルで実行する.
    df_std=df
    df_std["Area"]=data_std
    result_messeges.append(Linear_svc.fit_k_folds(df_std))

    for i, r in enumerate(result_messeges[0]):
        print(f"default: \n{r}\nstandardization: \n{result_messeges[1][i]}\n")


if __name__=="__main__":
    main()

