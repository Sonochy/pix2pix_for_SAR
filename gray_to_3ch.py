from PIL import Image
import numpy as np
import os
from tqdm import tqdm
Image.MAX_IMAGE_PIXELS = 1000000000
# 元となる画像の読み込み
np.set_printoptions(threshold=np.inf)
if not os.path.exists("./gray_to_3ch"):
    os.mkdir("./gray_to_3ch/output")


for i in tqdm(range(80)):
    num ='{0:02d}'.format(i)
    img = Image.open('./gray_to_3ch/input/train_'+num+'.jpg')
    gray_3ch = img.convert("RGB")
    #label = label.resize((1024, 1024))#リサイズ
    #label.putpalette(palette)
    #label.convert("RGB")

    number_padded = '{0:02d}'.format(i)
    gray_3ch.save(os.path.join("./gray_to_3ch/output/", ("train_" + number_padded + ".png")))
