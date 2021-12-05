# はじめに

```{only} html
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/chokkan/mlnote/blob/main/)
[![Open In Studio Lab](https://studiolab.sagemaker.aws/studiolab.svg)](https://studiolab.sagemaker.aws/import/github/chokkan/mlnote/blob/master/classification/01binary.ipynb)
[![badge](https://img.shields.io/badge/launch-binder-579ACA.svg?logo=data:image/png;base64,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)](https://mybinder.org/v2/gh/chokkan/mlnote/main)
[![Jupyter Book Badge](https://jupyterbook.org/_images/badge.svg)](https://jupyterbook.org)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![made-with-numpy](https://img.shields.io/badge/Made%20with-NumPy-1f425f.svg)](https://numpy.org/)
[![made-with-matplotlib](https://img.shields.io/badge/Made%20with-Matplotlib-1f425f.svg)](https://matplotlib.org/)
[![made-with-scikit-learn](https://img.shields.io/badge/Made%20with-scikit--learn-1f425f.svg)](https://scikit-learn.org/)
[![made-with-pytorch](https://img.shields.io/badge/Made%20with-PyTorch-1f425f.svg)](https://pytorch.org/)
```

機械学習帳は、**機械学習**を学ぶためのノート（**帳**）を、デジタル（**機械**）による新しいカタチの**学習帳**として実現することを目指しています。

:::{panels}
:container: +full-width
:column: col-lg-6 px-2 py-2
:card:

👩‍💻 **理論と実装を一体化した「動く」学習帳** 👨‍💻
^^^
機械学習の理論と実装を一緒に説明することで、理論の実装や応用に触れるだけでなく、プログラムの実行例を通して理論への理解を深めることができます。

<div style="text-align: center;">
<video autoplay loop muted playsinline width="100%" src="sgd.mp4"></video>
</div>

---
**プログラミング言語としてPythonを採用** ✨
^^^
機械学習や深層学習の研究開発でよく用いられる[Python](https://www.python.org/)をプログラミング言語として採用しています。[NumPy](https://numpy.org/), [Matplotlib](https://matplotlib.org/), [scikit-learn](https://scikit-learn.org/), [scipy](https://scipy.org/), [PyTorch](https://pytorch.org/)などのエコシステムとあわせて、機械学習の実装を習得できます。

```python
import torch

x = torch.tensor([1., -1.])
w = torch.tensor([1.0, 0.5], requires_grad=True)

loss = -torch.dot(x, w).sigmoid().log()
loss.backward()
print(loss.item())
print(w.grad)
```

---
**機械学習の基礎事項を学べる** 📖
^^^
機械学習帳は、単回帰、重回帰、ロジスティック回帰、ニューラルネットワーク、サポートベクトルマシン、クラスタリング、主成分分析、確率的勾配降下法、正則化など、機械学習の重要事項を広くカバーしています。初学者向けに、その原理や数学的な取り扱いを丁寧に説明します。

---
**オープンソース・プロジェクト** 🎁
^^^
機械学習帳は、[クリエイティブ・コモンズ 表示 - 非営利 - 改変禁止 4.0 国際 (CC BY-NC-ND 4.0)](https://creativecommons.org/licenses/by-nc-nd/4.0/deed.ja)（プログラム部分以外）および[MITライセンス](https://opensource.org/licenses/MIT)（プログラム部分）で公開されているオープンソース・プロジェクトです。不具合報告はGitHubの[issues](https://github.com/chokkan/mlnote/issues)までお願いします。

:::

機械学習帳は、[Jupyter Lab](https://jupyter.org/#jupyterlab)で書かれたコンテンツを[Jupyter Book](https://jupyterbook.org/)で変換することで生成されています。

## 講義

+ 東京工業大学情報理工学院 [機械学習 (CSC.T254)](http://www.ocw.titech.ac.jp/index.php?module=General&action=T0300&JWC=202127792)
