#!/usr/bin/env python3
# coding: utf-8

import glob
import re
import os
import argparse
import shutil

print("保存先のフォルダー名を指定してください。.......")
FOLDER_NAME = str(input())

def main0():
    if not os.path.exists(FOLDER_NAME):#ディレクトリがなかったら
        os.mkdir(FOLDER_NAME)#作成したいフォルダ名を作成

def main1():
    # parserを作成
    parser = argparse.ArgumentParser()
    parser.add_argument('dir_path', help='designate dir path')
    args = parser.parse_args()

    # ワイルドカードで条件を満たすパスの文字列を指定
    pathlist1 = glob.glob(args.dir_path + '/*.json')

    # python3.5以降 サブディレクトリも検索
    # **の部分があらゆる中間ディレクトリに対応
    pathlist2 = glob.glob(args.dir_path + '/**/*.json', recursive=True)

    # ファイル名のみを取得
    pathlist3 = [os.path.basename(p) 
    for p in glob.glob(args.dir_path + '/**', recursive=True) 
    if os.path.isfile(p)]

    for path in pathlist2:
        if '.json' in path:
            a = path.split('/')
            print(str(a[-1]) + "：ファイルをコピーいしています.")
            shutil.copy2(str(path),  FOLDER_NAME + "/" + str(a[-1]) )

if __name__ == '__main__':
    main0()
    main1()
