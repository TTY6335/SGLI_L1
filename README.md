# このプログラム?  
JAXA GCOM-C SGLIのLevel 1のHDF5ファイルをgeotiffに変換と地図投影するpythonプログラムです。
# 環境  
 開発環境は以下です。
* CentOS Linux release 7.7.1908 (Core)
* python 3.7.4
* h5py 2.9.0
* hdf5 1.10.4
* numpy 1.16.5
* gdal 1.11.4


# 使い方
`python3 L1.py path_to_L1.h5 path_to_out.tif`  
RGBカラーに対応するRV03,RV05,RV08を抜き出して1ファイルにします。 他のバンドを抜き出す方法はwikiを参照してください。

# 注意事項
~gcpを与えるときに標高を考慮していません。~  
地球固定座標系に投影しているプロダクトなので、標高は考慮されていません。
open street mapなどと比較したとき、海岸線は合うと思いますが、標高の高い地域では位置ずれが発生します。
SRTMやAW3DなどのDSMから標高データを元に標高データをgcpに与える必要があります。  
  
かなりメモリを使います。メモリ8GB以上の環境での実行をおすすめします。
