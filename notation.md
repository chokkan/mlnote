# 表記

$\def\bm{\boldsymbol}$機械学習帳では，以下の数学の記法を採用しています．

| 表記 | 説明 |
|:-:|:--|
| $a$ | スカラー |
| $\bm{a}$ | ベクトル（断りがない限り列ベクトル） |
| $a_i$ | ベクトル$\bm{a}$の$i$番目の要素（先頭の要素は$1$番目） |
| $\bm{A}$ | 行列 |
| $A_{i,j}$ | 行列$\bm{A}$の$i$行$j$列の要素 |
| $\bm{A}_{i,:}$ または $\bm{A}_{i}$ | 行列$\bm{A}$の$i$行ベクトル |
| $\bm{A}_{:,j}$ | 行列$\bm{A}$の$j$列ベクトル |
| $\bm{I}_n$ | $n \times n$の単位行列 |
| $\bm{I}$ | 単位行列（大きさは文脈から推測する） |
| $\bm{A}^\top$ | 行列$\bm{A}$の転置 |
| $\bm{A}^{-1}$ | 行列$\bm{A}$の逆行列 |
| $\bm{A}^{+}$ | 行列$\bm{A}$のムーア・ペンローズの疑似逆行列 |
| ${\rm diag}(\bm{a})$ | 対角成分が$\bm{a}$で構成される対角行列 | 
| $\mathbb{R}$ | 実数の集合 |
| $\mathbb{C}$ | 複素数の集合 |
| $\mathbb{N}_n$ | 自然数の集合$\{1, 2, \dots, n\}$ |

以下の変数はおおよそ一貫した意味で用いられます．

| 表記 | 説明 |
|:-:|:--|
| $d$ | ひとつの事例を表現する説明変数の数（特徴空間の次元数） |
| $K$ | ひとつの事例を表現する目的変数の数（ラベルの数） |
| $N$ | データに含まれる事例数 |
| $x$ | 入力変数（説明変数の数は一つ） |
| $\bm{x} \in \mathbb{R}^d$ | 入力ベクトル（説明変数の数は$d$個） |
| $\bm{X} \in \mathbb{R}^{N \times d}$ | 入力ベクトルを縦に積んで行列にしたもの |
| $y$ | 出力変数（目的変数の数は一つ） |
| $\bm{y} \in \mathbb{R}^K$ | 出力ベクトル（目的変数の数は$K$個） |
| $\bm{Y} \in \mathbb{R}^{N \times K}$ | 出力ベクトルを縦に積んで行列にしたもの |
| $\mathcal{D}$ | データ（事例の集合） |
