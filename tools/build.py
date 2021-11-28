#!/bin/python
import glob
import os
import re
import shutil
import sys

twitter_card = """
    <meta name="twitter:card" content="summary">
    <meta name="twitter:site" content="@chokkanorg">
    <meta name="twitter:title" content="機械学習帳">
    <meta name="twitter:description" content="機械学習帳は、機械学習を学ぶためのノート（帳）を、デジタル（機械）による新しいカタチの学習帳として実現することを目指しています。">
    <meta name="twitter:image" content="https://chokkan.github.io/python/_static/mlnote.png">

    <!-- Google Analytics -->
"""

def build():
    os.system('jupyter-book build --all .')
    shutil.copyfile('./regression/sgd.mp4', './_build/html/sgd.mp4')

def add_twitter_card():
    shutil.copyfile('./material/mlnote.png', './_build/html/_static/mlnote.png')
    for src in glob.glob('_build/html/*.html'):
        with open(src) as fi:
            content = fi.read()
        content = content.replace('<!-- Google Analytics -->', twitter_card)
        with open(src, 'w') as fo:
            fo.write(content)

def update_license():
    for src in glob.glob('*.ipynb'):
        with open(src) as fi:
            content = fi.read()
        with open(src, 'w') as fo:
            fo.write(content)

if __name__ == '__main__':
    #update_license()
    build()
    add_twitter_card()
