# -*- coding: utf-8 -*-
import random
import PIL.Image as Image
import os
import argparse

suffixs = ['.jpg','.png']


def args_parse():
    parser = argparse.ArgumentParser(description='image merge')
    parser.add_argument('-path',nargs='?',dest='path',default=os.getcwd(),type=str)
    parser.add_argument('-uw',nargs='?',dest='uw',default=120,type=int)
    parser.add_argument('-uh',nargs='?',dest='uh',default=120,type=int)
    parser.add_argument('-cn',nargs='?',dest='cn',default=5,type=int)
    parser.add_argument('-margin',nargs='?',dest='margin',default=4,type=int)
    parser.add_argument('-bg',nargs='?',dest='bg',choices=['w','b'],default='w',type=str)

    return parser.parse_args()

def walk_dir(path):
    selected_files = []
    for root,dirs,files in os.walk(path):
        for f in files:
            path_to_file = os.path.join(root, f)
            filename, ext = os.path.splitext(f)

            if ext.lower() in suffixs:
                selected_files.append(path_to_file)

    return selected_files

def shuff_file(files):
    for i in range(0,len(files)):
        x = random.randint(0,len(files)-1)
        temp = files[i]
        files[i] = files[x];
        files[x] = temp;
    return files

def merge(files, uw, uh, cn, margin, bg):

    num_of_img = len(files)


    rn = num_of_img / cn
    if num_of_img > rn * cn:
        rn += 1

    width_of_target = uw * cn + (cn+1)*margin
    height_of_target = uh * rn + (rn+1)*margin
    quality_value = 100

    target = Image.new("RGBA",(width_of_target,height_of_target),bg)

    step_width = uw + margin
    step_height = uh + margin

    left = margin
    top = margin

    count = 0
    for f in files:
        img = Image.open(f);
        img = img.resize((uw ,uh), Image.ANTIALIAS)

        target.paste(img, (left, top))
        left += step_width

        count += 1
        if count == cn:
            count = 0
            left = margin
            top += step_height

    target.save("result.jpg", quality=quality_value)
    print 'done'

if __name__ == '__main__':
    try:
        os.remove(os.path.join(os.getcwd(),'result.jpg'))
    except OSError:
        pass
    args = args_parse()
    base_path = args.path # 图片所在路径
    uw = args.uw    # unit_width 小图片宽度
    uh = args.uh    # unit_height 小图片高度
    cn = args.cn    # 每行列数
    margin = args.margin    # 行间距，也是列间距

    bg = args.bg    # 背景颜色
    if bg=='w':
        bg=(255,255,255,0)
    else:
        bg=(0,0,0,0)

    files = walk_dir(base_path)
    files = shuff_file(files)

    merge(files,uw,uh,cn,margin,bg)




