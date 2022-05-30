import pandas as pd
import numpy as np

def load_dataset():
    """ 
    学習するデータセットをpandas型で読み込む.

    args:
        None
    
    return:
        DataFrame df; 学習に使うデータセット
     """
    #学習データを読み込む
    df = pd.read_excel("../../rep1/temp/data/Raisin_Dataset/Raisin_Dataset.xlsx")
    
    return df

def div_dataset(df):
    """ 
    データセットを特徴ベクトルと教師データに分割する.

    args:
        DataFrame df: 分割する対象のデータセット

    return:
        ndarray X; 特徴データ
        ndarray y: 教師データ
     """
    y = df['Class'].values
    X = df.drop(columns='Class').values #'Class'カラムを除いたデータ。

    return X,y


    
