from sklearn.svm import LinearSVC
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
import dataset

#linearSVCのハイパーパラメータのうちCについて、0.5, 0.1, 1.5の3つを考える.
def fit_k_folds(data):
    """ 
    引数 data に対して、5分割交差検証を行う.

    args:
        DataFrame data; 学習の対象となるデータセット

    return:
        list res; 学習結果を示すテキストメッセージの集まり
     """
    Cs = [0.5, 1.0, 1.5]
    
    #学習データと、目標データを取得。
    X, y = dataset.div_dataset(data)
    

    k_folds = 5 # ５分割検定

    res=[]

    for c in Cs:
        model = LinearSVC(C=c)

        #学習用データセットを５個のデータセットに分割し、テストデータとの学習を行う。学習データ内のサンプルは毎回シャッフルされる。
        scores = cross_val_score(model, X, y, cv=KFold(n_splits=k_folds, shuffle=True)) 
        #.mean()で平均値を算出。
        average = scores.mean()
        res.append(f'C = {c}: \nscores={scores}, average={average:.3f}')

    return res