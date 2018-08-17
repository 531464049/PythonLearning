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
        # 分割出目录与文件
        file_path = os.path.split(path)
        # 分割出文件与文件扩展名
        lists = file_path[1].split('.')
        # # 文件名
        fileName = lists[0]
        # 后缀
        file_ext = lists[-1]
        img_ext = ['jpeg', 'png', 'jpg']
        print(lists[0])
        # fileNmewName = fileName.replace('bz_2_2_o_ut', 'bz_3_3_p_u_t')
        # os.rename(path, file_path[0] + '/' + fileNmewName + '.' + file_ext)

        if file_ext in img_ext:
            fileNmewName = fileName.replace('_b_z_n_2_89_io_yu_7_', '_b_z_3_n_34_sfo_p_x_')
            os.rename(path, file_path[0] + '/' + fileNmewName + '.' + file_ext)

    elif os.path.isdir(path):
        for x in os.listdir(path):
            # os.path.join()在路径处理上很有用
            change_name(os.path.join(path, x))


def main():
    img_dir = '/Users/mahao/Desktop/images'
    start = time.time()
    change_name(img_dir)
    c = time.time() - start
    print('程序运行耗时:%0.2f' % (c))


if __name__ == '__main__':
    main()