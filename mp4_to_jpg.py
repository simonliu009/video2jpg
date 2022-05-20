#!/usr/bin/env python
# -*- coding:utf-8 -*-
###
# File: /Users/simonliu/Documents/K210_Sipeed_Maixpy/mp4_to_jpg.py
# Project: /Users/simonliu/Documents/K210_Sipeed_Maixpy
# Created Date: 2022-05-07 18:23:39
# Author: Simon Liu
# -----
# Last Modified: 2022-05-20 17:07:59
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
     


def Video2Pic():
    videoPath = "./res.mp4"  # 读取视频路径
    imgPath = "jpg/"  # 保存图片路径
 
    cap = cv2.VideoCapture(videoPath)
    fps = cap.get(cv2.CAP_PROP_FPS)  # 获取帧率
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # 获取宽度
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 获取高度
    suc = cap.isOpened()  # 是否成功打开
    frame_count = 0
    while suc:
        frame_count += 1
        suc, frame = cap.read()
        #cv2.imwrite(imgPath + str(frame_count).zfill(4), frame)
        cv2.imwrite(imgPath + "%d.jpg" %frame_count, frame)
        cv2.waitKey(1)
    cap.release()
    print("视频转图片结束！")
     
     
if __name__ == '__main__':
    Video2Pic()
    #Pic2Video()
