from cProfile import label
import matplotlib.pyplot as plt
import pandas as pd


def plot(df,df_std):
    """ 
    標準化前と後のデータセットを可視化する.

    args:
        DataFrame df; プロットする標準化前のデータセット
        DataFrame df_std; プロットする標準化後のデータセット

    return:
        None
     """
    fontsize = 16
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10,10))
    fig.subplots_adjust(hspace=0.4)


    # 画像1の設定
    ax1.tick_params(labelsize=fontsize)
    ax1.set_title('default', fontsize=fontsize)
    ax1.set_xlabel('sample', fontsize=fontsize)
    ax1.set_ylabel('value', fontsize=fontsize)

    #画像2の設定
    ax2.set_title('standaridization', fontsize=fontsize)
    ax2.set_xlabel('sample', fontsize=fontsize)
    ax2.set_ylabel('value', fontsize=fontsize)

    # columnsを抽出
    cols = df.columns.delete(-1)
    for col in cols:
        # default values
        df[f'{col}'].plot(ax=ax1, label=f'{col}')
    
        # standardization
        df_std[f'{col}'].plot(ax=ax2, label=f'{col}')


    plt.legend()
    # 描画した画像をpng保存
    plt.savefig("plot2.png", format="png", dpi=300)