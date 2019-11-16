# coding:utf-8
#L1B_VNR_NP 可視近赤外（非偏光）をバンド毎にtiffにする
import h5py
import numpy as np
import os, sys
import tifffile

input_dir='./'
input_file='GC1SG1_201904061259G27117_1BSG_VNRDK_1004.h5'
input_data=input_dir+input_file

f=h5py.File(input_data,'r')

lat_arr=np.array(f['Geometry_data']['Latitude'])
lon_arr=np.array(f['Geometry_data']['Longitude'])

#GCPのメモをつくる。gdal_translateでつかうことになる。
memo="gcp_memo.txt"
txt=open(memo,'w')
for column in range(0,lat_arr.shape[0]-1,10):
    for row in range(0,lat_arr.shape[1]-1,10): 
#        print(column*10,row*10,lat_arr[column][row],lon_arr[column][row])
        txt.write("-gcp "+str(row*10)+" "+str(column*10)+" "+str(lon_arr[column][row])+" "+str(lat_arr[column][row])+"\n")
txt.close()

#upper_left_lat=f['Geometry_data'].attrs['Upper_left_latitude']
#upper_left_lon=f['Geometry_data'].attrs['Upper_left_longitude']
#upper_right_lat=f['Geometry_data'].attrs['Upper_right_latitude']
#upper_right_lon=f['Geometry_data'].attrs['Upper_right_longitude']
#lower_left_lat=f['Geometry_data'].attrs['Lower_left_latitude']
#lower_left_lon=f['Geometry_data'].attrs['Lower_left_longitude']
#lower_right_lat=f['Geometry_data'].attrs['Lower_right_latitude']
#lower_right_lon=f['Geometry_data'].attrs['Lower_right_longitude']
#print("lat,lon")
#print(upper_right_lat,upper_right_lon)

band_list=['Lt_VN01','Lt_VN02','Lt_VN03','Lt_VN04','Lt_VN05','Lt_VN06','Lt_VN07','Lt_VN08','Lt_VN09','Lt_VN10','Lt_VN11']
for band in band_list:
    print(band)
    band_image_arr=f['Image_data'][band]
    print(band_image_arr.shape)
    slope=f['Image_data'][band].attrs['Slope']
    offset=f['Image_data'][band].attrs['Offset']
    Slope_reflectance=f['Image_data'][band].attrs['Slope_reflectance']
    Offset_reflectance=f['Image_data'][band].attrs['Offset_reflectance']
    #numpyの行列にする
    band_image_arr=np.array(band_image_arr,dtype='uint16')
    #MSBを0にする
    band_image_arr=np.where(band_image_arr>=32768,band_image_arr-32768,band_image_arr)
    #15ビット目を0にする
    band_image_arr=np.where(band_image_arr>=16384,band_image_arr-16384,band_image_arr)
    #欠損値をnanで埋める 0で埋めたときよりもgdal_translateの処理が速くなる?
    band_image_arr=np.where(band_image_arr==16383,np.nan,band_image_arr)
#    #大気上端放射輝度を求める
#    Lt=slope*band_image_arr+offset
    #大気上端反射率を求める
    Rt=Slope_reflectance*band_image_arr+Offset_reflectance
    #出力
    output_file_path="output/"
    output_filename=input_file[:-3]+"_Rt"+band[2:]+".tif"
    output_file=output_file_path+output_filename
    tifffile.imsave(output_file,Rt)

f.close()
