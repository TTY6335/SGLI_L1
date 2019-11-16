#!/bin/sh

#入力するファイル名
input_file=output/GC1SG1_201904061259G27117_1BSG_VNRDK_1004_Rt_VN08.tif
#出力ファイル名
output_file=Rt_VN08.tif
#GCPを画像に張り付ける
gdal_translate -of "GTiff" --optfile gcp_memo.txt $input_file tmp1.tif
#幾何補正
#gdalwrapの処理中に警告がでるけどたぶん大丈夫
#幾何補正して画像サイズが変わるのに余白がなかったりすることが原因らしい
#メモリをたくさん確保する
#8GB確保してみる
#gdalwarp --config GDAL_CACHEMAX 8192 -tps -t_srs EPSG:4326 -of "GTiff" -dstnodata 0 tmp1.tif $output_file
gdalwarp --config GDAL_CACHEMAX 4096 --config GDAL_SWATH_SIZE 256000000 \
-tps -t_srs EPSG:4326 -of "GTiff" -dstnodata None tmp1.tif $output_file
