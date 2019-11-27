#!/usr/bin/python
'''
# http://portaltan.hatenablog.com/entry/2018/11/01/175955
import numpy as np
import cv2

# image info
image_file = './binary_test.png'
img = cv2.imread(image_file)

# detect blue
# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower = np.array([0, 0, 0])
upper = np.array([255, 0, 0])
img_mask = cv2.inRange(img, lower, upper)
img_color = cv2.bitwise_and(img, img, mask=img_mask)

# debug
cv2.imwrite("ika_hsv.jpg", img_color)
'''

# -*- coding: utf-8 -*-
# https://qiita.com/Morio/items/f34dab8825c9d76664f5
from __future__ import print_function
import os
import numpy as np
import argparse
import cv2
from tqdm import tqdm

def parse_args():
    #コマンドラインオプションの定義
    # https://docs.python.org/ja/3/library/argparse.html
    parser = argparse.ArgumentParser(description='make file list')
    # --dataを定義,
    # dest:parse_args() が返すオブジェクトに追加される属性名。e.g.:args.data_dir
    # default:コマンドラインに引数がなかった場合に生成される値。
    parser.add_argument('--name', dest='list_name', default='list')
    parser.add_argument('--input_path', dest='input_dir', default='./RGB_to_binary/input')
    parser.add_argument('--output_path', dest='output_dir', default='./RGB_to_binary/output')
    args = parser.parse_args()
    return args

args = parse_args()

INPUT_PATH = args.input_dir
OUTPUT_PATH = args.output_dir

data_list = []

for file in tqdm(os.listdir(INPUT_PATH)):
    if file == '.DS_Store':
        continue

    else:
        img = cv2.imread(os.path.join(INPUT_PATH + '/' + file))
        # print(os.path.join(INPUT_PATH + '/' + file))
        lower = np.array([20, 0, 0])     # (B,R,G)
        upper = np.array([255, 30, 30])
        img_mask = cv2.inRange(img, lower, upper)
        img_color = cv2.bitwise_and(img, img, mask=img_mask)

        # グレースケールに変換する。
        gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
        # 2値化する。
        _, binary = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)

        median_binary = cv2.medianBlur(binary, 3)





        bname, ext = os.path.splitext(file)

        cv2.imwrite(os.path.join(OUTPUT_PATH + '/' + file), median_binary)

        # debug
        #cv2.imwrite(os.path.join(OUTPUT_PATH + '/' + file), median_binary)
        # cv2.imwrite(os.path.join(OUTPUT_PATH + '/' + file), img_color)