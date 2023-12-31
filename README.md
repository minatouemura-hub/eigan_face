# SVDによる画像の情報量削減

## 目的

このプロジェクトの目的は、Single Value Decomposition（SVD）を使用して画像の情報量を削減し、次にPrincipal Components Analysis（PCA）を用いて画像の次元数を削減することです。このプロジェクトは、ストラング先生の講義で学んだ理論を実際の画像に適用することを目指しています。

## プロジェクト構成

1. **config.py**: プロジェクトの設定を管理するためのファイルです。ここで、画像のパスやSVD、PCAなどのパラメータを設定します。

2. **utils.py**: ユーティリティ関数が含まれています。画像の読み込み、SVD、PCAなど、プロジェクト全体で使用される関数がここに含まれます。

3. **main.py**: メインの実行ファイルです。ここで、config.pyおよびutils.pyから関数やパラメータを呼び出し、画像の情報量削減のプロセスを実行します。

## パッケージ

1. **numpy**: 行列操作や数学的計算のための基本的なパッケージです。

2. **argparse**: コマンドライン引数を解析するためのパッケージです。これにより、main.pyが実行される際に様々な設定を変更できます。

## プロジェクトの実行

以下は、プロジェクトの実行手順です。

1. `config.py`ファイルを編集し、画像のパスやどの程度、画素数を落とすかを決めます

2. コマンドラインで`main.py`を実行します。例えば：

   ```bash
   python main.py --path img.png
   ```

3. プログラムはSVDを使用して画像の情報量を削減し、結果を保存します。

## 注意事項

- このプロジェクトはPython 3環境で動作します。

## 今後の展望

次に、Principal Components Analysis（PCA）を用いて画像の次元数を削減する予定です。これにより、より効率的に画像の情報を圧縮し、次元削減の手法の理解を深めます。

以上が、SVDによる画像の情報量削減プロジェクトの基本的な構成と手順です。
