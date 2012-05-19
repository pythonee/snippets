# -*- coding: utf-8 -*-
import random
import PIL.Image as Image
import os,sys
from itertools import chain

suffixs = ['.jpg','.png']

def walk_dir(path):
    selected_files = []
    for root,dirs,files in os.walk(path):
        for f in files:
            path_to_file = os.path.join(root, f)
            filename, ext = os.path.splitext(f)
            
            if ext.lower() in suffixs:
                selected_files.append(path_to_file)

    return selected_files

def get_base_path():
    base_path = ''
    if len(sys.argv) >= 2:
        base_path = sys.argv[1]
    else:
        base_path = os.getcwd()
    return base_path


def shuff_file(files):
    for i in range(0,len(files)):
        x = random.randint(0,len(files)-1)
        temp = files[i]
        files[i] = files[x];
        files[x] = temp;
    return files

def merge(files):
    UNIT_WIDTH = 120 #每张图片宽度
    UNIT_HEIGHT = 120 #每张图片高度
    IMG_OF_ROW = 6 # 每行图片数

    COLS = 4  # 间隙
    

    NUM_OF_IMG = len(files)
    
    
    NUM_OF_ROW = NUM_OF_IMG / IMG_OF_ROW
    if NUM_OF_IMG > NUM_OF_ROW * IMG_OF_ROW:
        NUM_OF_ROW += 1
        
    WIDTH_OF_TARGET = UNIT_WIDTH * IMG_OF_ROW + (IMG_OF_ROW+1)*COLS
    HEIGHT_OF_TARGET = UNIT_HEIGHT * NUM_OF_ROW + (NUM_OF_ROW+1)*COLS
    QUALITY_VALUE = 100
       
    target = Image.new("RGBA",(WIDTH_OF_TARGET,HEIGHT_OF_TARGET))
    
    STEP_WIDTH = UNIT_WIDTH + COLS
    STEP_HEIGHT = UNIT_HEIGHT + COLS

    left = COLS
    top = COLS
    
    count = 0
    for f in files:
        img = Image.open(f);
        img = img.resize((UNIT_WIDTH, UNIT_HEIGHT), Image.ANTIALIAS)

        target.paste(img, (left, top))
        left += STEP_WIDTH

        count += 1
        if count == IMG_OF_ROW:
            count = 0
            left = COLS
            top += STEP_HEIGHT
            
    target.save("result.jpg", quality=QUALITY_VALUE)
    print 'done'

if __name__ == '__main__':
    try:
        os.remove(os.path.join(os.getcwd(),'result.jpg'))
    except OSError:
        pass
    base_path = get_base_path()
    files = walk_dir(base_path)
    files = shuff_file(files)
    
    merge(files)

        
    
        
