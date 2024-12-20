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
    <meta name="twitter:image" content="https://chokkan.github.io/mlnote/_static/mlnote.png">
    </head>
"""

sagemaker_studio_lab = """
<span class="btn__text-container">Colab</span>
</a>
</li>

<li>
    <a href="https://studiolab.sagemaker.aws/import/github/chokkan/python/blob/main/{}"
       class="btn btn-sm dropdown-item"
       title="Launch on SageMaker Studio Lab"
       data-bs-placement="left" data-bs-toggle="tooltip">

<span class="btn__icon-container">
  <i class="fab fa-aws"></i>
</span>
<span class="btn__text-container">SageMaker</span>
"""

def build():
    os.system('jupyter-book build --all .')
    shutil.copyfile('./regression/sgd.mp4', './_build/html/sgd.mp4')

def modify_html():
    # Copy the Twitter card.
    shutil.copyfile('./material/mlnote.png', './_build/html/_static/mlnote.png')

    # Modify the generated HTML files.
    for src in glob.glob('_build/html/**/*.html', recursive=True):
        print(f'Updating: {src}')
        
        # Load the HTML content.
        with open(src) as fi:
            content = fi.read()
            
        # Find the path to .ipynb
        path = ''
        m = re.search(r'"https://colab\.research\.google\.com/github/chokkan/mlnote/blob/main/([^"]+)"', content)
        if m is not None:
            path = m.group(1)
            print(f'    path: {path}')
        
        # Add meta tags for Twitter card.
        content = content.replace('</head>', twitter_card)
        
        # Add the button for SageMaker Studio Lab.
        if path:
            content = content.replace(
                '<span class="btn__text-container">Colab</span>',
                sagemaker_studio_lab.format(path)
                )
        
        # Write out the HTML content.
        with open(src, 'w') as fo:
            fo.write(content)

def update_license():
    for src in glob.glob('*/*.ipynb'):
        print('Updating:', src)
        with open(src) as fi:
            content = fi.read()
            content = content.replace('Copyright 2020-2022', 'Copyright 2020-2024')
        with open(src, 'w') as fo:
            fo.write(content)

if __name__ == '__main__':
    #update_license()
    build()
    modify_html()
