# This program?  
JAXA GCOM-C SGLIのLevel 1のHDF5ファイルをgeotiffに変換と地図投影するpythonプログラムです。  
This is a Python program for converting JAXA GCOM-C SGLI Level 1 HDF5 files to GeoTIFF format and performing map projection.

# Environment  
 開発環境は以下です。 The development environment is as follows:  
* CentOS Linux release 7.7.1908 (Core)
* python 3.7.4
* h5py 2.9.0
* hdf5 1.10.4
* numpy 1.16.5
* gdal 1.11.4


# Usage
`python3 L1.py path_to_L1.h5 path_to_out.tif`  
RGBカラーに対応するRV03,RV05,RV08を抜き出して1ファイルにします。 他のバンドを抜き出す方法はwikiを参照してください。  
It extracts RV03, RV05, and RV08, which correspond to RGB colors, and saves them as a single file. For extracting other bands, please refer to the wiki.

# Notes 
~gcpを与えるときに標高を考慮していません。~  
地球固定座標系に投影しているプロダクトなので、標高は考慮されていません。
open street mapなどと比較したとき、海岸線は合うと思いますが、標高の高い地域では位置ずれが発生します。
SRTMやAW3DなどのDSMから標高データを元に標高データをgcpに与える必要があります。  
  
かなりメモリを使います。メモリ8GB以上の環境での実行をおすすめします。

It does not consider elevation when providing GCP (Ground Control Points).
Since the product is projected onto a fixed Earth coordinate system, elevation is not taken into account.
The coastline should match when compared to sources like OpenStreetMap, but there may be positional discrepancies in high-altitude regions.
You will need to provide elevation data to the GCP using a DSM (Digital Surface Model) such as SRTM or AW3D.

It requires a significant amount of memory. It is recommended to run it in an environment with 8GB of memory or more.
