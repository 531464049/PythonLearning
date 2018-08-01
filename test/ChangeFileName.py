#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : mh
import time
import os


def change_name(path):
    if not os.path.isdir(path) and not os.path.isfile(path):
        print("路径错误")
        return
    if os.path.isfile(path):
        file_path = os.path.split(path)  #分割出目录与文件
        lists = file_path[1].split('.')  #分割出文件与文件扩展名
        file_ext = lists[-1]  #取出后缀名(列表切片操作)
        img_ext = ['jpeg', 'png', 'jpg']
        if file_ext in img_ext:
            os.rename(path,
                      file_path[0] + '/' + 'bzjk' + lists[0] + '.' + file_ext)

    elif os.path.isdir(path):
        for x in os.listdir(path):
            change_name(os.path.join(path, x))  #os.path.join()在路径处理上很有用


def main():
    img_dir = '/Users/mahao/Desktop/1111'
    start = time.time()
    change_name(img_dir)
    c = time.time() - start
    print('程序运行耗时:%0.2f' % (c))


if __name__ == '__main__':
    main()