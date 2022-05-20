#!/usr/bin/env python
# -*- coding:utf-8 -*-
###
# File: /Users/simonliu/Documents/python/video2jpg/video_to_jpg.py
# Project: /Users/simonliu/Documents/python
# Created Date: 2022-05-07 18:23:39
# Author: Simon Liu
# -----
# Last Modified: 2022-05-20 19:07:47
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
basename = str(src_path.stem)
dst_path = src_path.parent/f'{basename}_frames'
# Option to decide whether to save frame to independent folders ，每个视频帧是否保存在独立文件夹，默认为False
independent_folder = False
# Skip {frame_to_skip} frames before saving another frame ，保存图片的间隔帧数
frame_to_skip = 5
total_saved = 0

file_types = ['MOV','MP4','AVI','FLV']

def browse_video_files(dir):
    filecount = 0
    global file_types,total_saved
    if dir.exists():
        print('找到源视频文件夹:',dir)
        for f in dir.glob('**/*'):
            if(f.is_file() and (f.suffix.upper()[1:] in file_types)):
                print('正在转换文件 ------->>>',f.name)
                video2pic(f)
                filecount += 1
            else:
                pass
    else:
        print('文件夹不存在:',str(dir))
    print(f'总共转换了{filecount}个文件, 提取了{total_saved}帧图片。')

def video2pic(f):
    global src_path,dst_path,frame_to_skip,total_saved
    filename = f.stem #获取文件名，不含后缀
    cap = cv2.VideoCapture(str(f))
    fps = cap.get(cv2.CAP_PROP_FPS)  # 获取帧率
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # 获取宽度
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 获取高度
    fcount = cap.get(cv2.CAP_PROP_FRAME_COUNT)      # 获取视频总帧数
    frame_to_save =  int(fcount/frame_to_skip)
    print(f'视频文件帧率：{fps}, 分辨率:{width}x{height},视频总帧数:{fcount},保存间隔帧率:{frame_to_skip},预计提取帧数:{frame_to_save}')
    suc = cap.isOpened()  # 是否成功打开
    frame_count = 0
    frame_saved = 0
    # dst_dir = f'{src_path}_frames/{filename}_frames'
    if independent_folder:
        dst_path = dst_path/f'{filename}_frames'
    print(f'目标文件夹:',dst_path)
    if dst_path.exists():
        # print(f'目标文件夹 {dst_path} 已经存在...')
        pass
    else:
        print(f'创建目标文件夹: {dst_path} ')
        dst_path.mkdir(exist_ok=True, parents=True)
    suc, frame = cap.read()
    while suc:
        frame_count +=  1
        if frame_count%frame_to_skip == 0:
            frame_saved += 1
            total_saved += 1
            print(f'正在写入 {dst_path}/{filename}_{frame_saved:05d}.jpg\r',end='')
            cv2.imwrite(f'{dst_path}/{filename}_{frame_saved:05d}.jpg', frame)
        suc, frame = cap.read()
        cv2.waitKey(1)
    cap.release()
    print(f'\n视频转图片结束！从视频 {f.name} 中提取了 {frame_saved} 帧画面。')
     
     
if __name__ == '__main__':
    browse_video_files(src_path)
