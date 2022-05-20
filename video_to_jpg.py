#!/usr/bin/env python
# -*- coding:utf-8 -*-
###
# File: /Users/simonliu/Documents/python/video2jpg/video_to_jpg.py
# Project: /Users/simonliu/Documents/python
# Created Date: 2022-05-07 18:23:39
# Author: Simon Liu
# -----
# Last Modified: 2022-05-20 17:02:20
# Modified By: Simon Liu
# -----
# Copyright (c) 2022 SimonLiu Inc.
# 
# May the force be with you.
# -----
# HISTORY:
# Date      	By	Comments
# ----------	---	----------------------------------------------------------
###
import cv2
from cv2 import VideoWriter, VideoWriter_fourcc, imread, resize
from pathlib import Path

src_dir = 'Movies/cat_video'
src_path = Path.home()/Path(src_dir)

filecount = 0
file_types = ['MOV','MP4','AVI','FLV']

def browse_video_files(dir):
    global filecount,file_types
    if dir.exists():
        print('找到源视频文件夹:',dir)
        for f in dir.glob("**/*"):
            if(f.is_file() and (f.suffix.upper()[1:] in file_types)):
                print("正在转换文件:",f)
                video2pic(f)
                filecount += 1
            else:
                pass
    else:
        print('文件夹不存在:',str(dir))

def video2pic(f):
    global src_path
    filename = f.stem #获取文件名，不含后缀
    cap = cv2.VideoCapture(str(f))
    fps = cap.get(cv2.CAP_PROP_FPS)  # 获取帧率
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # 获取宽度
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 获取高度
    print(f'视频文件帧率：{fps}, 分辨率:{width}x{height}')
    suc = cap.isOpened()  # 是否成功打开
    frame_count = 0
    dst_dir = f'{src_path}_frames/{filename}_frames'
    dst_path = Path.home()/Path(dst_dir)
    print(f'目标文件夹:',dst_path)
    if dst_path.exists():
        print(f'目标文件夹 {dst_path} 已经存在...')
    else:
        print(f'创建目标文件夹: {dst_path} ')
        dst_path.mkdir(exist_ok=True, parents=True)
    suc, frame = cap.read()
    while suc:
        frame_count += 1
        #cv2.imwrite(imgPath + str(frame_count).zfill(4), frame)
        print(f'正在写入 {dst_path}/{filename}_{frame_count:05d}.jpg\r',end='')
        cv2.imwrite(f'{dst_path}/{filename}_{frame_count:05d}.jpg', frame)
        suc, frame = cap.read()
        cv2.waitKey(1)
    cap.release()
    print(f"\n视频转图片结束！一共转换了{frame_count}帧画面。")
     
     
if __name__ == '__main__':
    browse_video_files(src_path)
