# -*- coding: utf-8 -*-
# https://qiita.com/Morio/items/f34dab8825c9d76664f5
# https://teratail.com/questions/11335
# https://stackoverflow.com/questions/19106894/how-to-save-pbm-image

from __future__ import print_function
import os
import numpy as np
import argparse
import cv2
from tqdm import tqdm
from natsort import natsorted
from PIL import Image



def parse_args():
    #コマンドラインオプションの定義
    # https://docs.python.org/ja/3/library/argparse.html
    parser = argparse.ArgumentParser(description='make file list')
    # --dataを定義,
    # dest:parse_args() が返すオブジェクトに追加される属性名。e.g.:args.data_dir
    # default:コマンドラインに引数がなかった場合に生成される値。
    parser.add_argument('--name', dest='list_name', default='list')
    parser.add_argument('--input_path', dest='input_dir', default='./Resize_original_size/input')
    parser.add_argument('--output_path', dest='output_dir', default='./Resize_original_size/output')
    parser.add_argument('--original_path', dest='original_dir', default='./Resize_original_size/original')
    args = parser.parse_args()
    return args

args = parse_args()

INPUT_PATH = args.input_dir
OUTPUT_PATH = args.output_dir
ORIGINAL_PATH = args.original_dir


data_list = []

# list_original = os.listdir(ORIGINAL_PATH).sort


for file_origin, file_input in tqdm(zip(natsorted(os.listdir(ORIGINAL_PATH)), natsorted(os.listdir(INPUT_PATH)) )):

    if file_input == '.DS_Store':
        continue

    else:
        origin_img = cv2.imread(os.path.join(ORIGINAL_PATH + '/' + file_origin))
        print(file_origin + " : " + file_input)

        # 画像の大きさを取得
        height, width = origin_img.shape[:2]
        # input_img = cv2.imread(os.path.join(INPUT_PATH + '/' + file_input))
        input_img = cv2.imread(os.path.join(INPUT_PATH + '/' + file_input), cv2.IMREAD_GRAYSCALE)
        resize_img = cv2.resize(input_img, dsize=(width, height))

        '''
        # 　インデックスカラー画像にするためにnumpyに変換
        resize_img = np.asarray(resize_img)
        # https://it-ojisan.tokyo/numpy-where-all-any/
        resize_img = np.where(resize_img == 255, 1, resize_img)
        # resize_img = resize_img.astype('bool8')
        print(resize_img.shape)
        #resize_img = resize_img.reshape(height, width, 1)
        print(resize_img.shape)
        '''


        bname, ext = os.path.splitext(file_input)

        '''
        pil_img = Image.fromarray(np.uint8(resize_img))
        pil_img.convert("L")
        pil_img.convert("P")
        pil_img.save(os.path.join(OUTPUT_PATH + '/' + file_input))
        '''

        #Image.fromarray(np.uint8(resize_img)).save(os.path.join(OUTPUT_PATH + '/' + bname + '.pbm'))

        '''
        # (8707, 10843, 3) 何故か3chある　reshapeする
        print(resize_img.shape)
        np.save(os.path.join(OUTPUT_PATH + '/' + bname), resize_img.astype('bool8'))
        '''


        '''
        # debug
        print(os.path.join(OUTPUT_PATH + '/' + bname + '.pbm'))
        cv2.imwrite(os.path.join(OUTPUT_PATH + '/' + bname + '.pbm'), resize_img)
        '''
        

        #print(os.path.join(OUTPUT_PATH + '/' + file_input))
        cv2.imwrite(os.path.join(OUTPUT_PATH + '/' + file_input), resize_img)



        # cv2.imwrite(os.path.join(OUTPUT_PATH + '/' + file), img_color)
