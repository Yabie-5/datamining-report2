import matplotlib.pyplot as plt

def plot(temp):
    """ 
    tempのデータを可視化する.
     """
    fontsize = 16
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10,10))
    fig.subplots_adjust(hspace=0.4)

    # default values
    temp['Eccentricity'].hist(ax=ax1, bins=100, log=True)
    ax1.tick_params(labelsize=fontsize)
    ax1.set_title('default', fontsize=fontsize)
    ax1.set_xlabel('Eccentricity', fontsize=fontsize)
    ax1.set_ylabel('Freqency', fontsize=fontsize)

    # standardization
    ax2.set_title('standaridization', fontsize=fontsize)
    ax2.set_xlabel('Eccentricity', fontsize=fontsize)
    ax2.set_ylabel('Freqency (log)', fontsize=fontsize)
    temp['standardization'].hist(ax=ax2, bins=100, log=True)
    #plt.hist(temp['standardization'], bins=100, log=True)

    plt.legend()
    # 描画した画像をpng保存
    plt.savefig("plot2.png", format="png", dpi=300)