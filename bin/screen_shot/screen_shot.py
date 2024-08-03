'''
Author: combofish combofish@163.com
Date: 2024-08-03 10:16:02
LastEditors: combofish combofish@163.com
LastEditTime: 2024-08-03 10:50:45
FilePath: \script-collection\bin\screen_shot\screen_shot.py
Description: 截屏脚本
'''
import numpy as np
from PIL import ImageGrab, Image
import cv2
import os.path as osp
import os
import pyautogui
import time


def shot_screen(shot_size=(0, 0, 1920, 1080), dst_path='./output', filename='screenshot1.jpg'):
    """截屏

    Args:
        shot_size (tuple, optional): 给定截屏尺寸. Defaults to (0, 0, 1920, 1080).
        dst_path (str, optional): 保存图片的路径. Defaults to './output'.
        filename (str, optional): 保存的文件名. Defaults to 'screenshot1.jpg'.
    """
    screen_width, screen_height = pyautogui.size()
    print(f'Screen (width,height): ({screen_width}, {screen_height})')

    if shot_size is None:
        shot_size = (0, 0, screen_width, screen_height)

    img = ImageGrab.grab(bbox=shot_size)  # bbox 定义左、上、右和下像素的4元组

    if not os.path.exists(dst_path):
        os.mkdir(dst_path)

    dst_file_name = osp.join(dst_path, filename)
    print(f'Shot with size {img.size}, Saving to {dst_file_name}')
    img.save(dst_file_name)


def shot_screens(dst_dir='./log'):
    cnt = 0
    while True:
        print(f'<<<  {cnt}  >>>')
        file_name = f'screenshot_{cnt}.jpg'

        shot_screen(filename=file_name, dst_path=dst_dir, shot_size=None)

        time.sleep(2)
        cnt = cnt + 1


if __name__ == '__main__':
    # shot_screen(shot_size=None)
    shot_screens('./log')
