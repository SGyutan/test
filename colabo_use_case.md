# Colabで自作のモジュールを読み込む


### Google Colaboratoryを使う方法

使い方の参照：

[Google Colabの使い方まとめ](https://qiita.com/shoji9x9/items/0ff0f6f603df18d631ab)

[Google Colabの使い方](https://interface.cqpub.co.jp/ail01/)

[Google Colabの使い方](https://lecture.ecc.u-tokyo.ac.jp/~ktanaka/algo20/google-colab/index.html)

[機械学習やるならGoogle Colabが素晴らしかった話（Python実行環境）  ](https://note.com/mc_kurita/n/n2a7c8682d965)


### Google Driveをマウント

作成したモージュールやサンプルデータを読み込むためのパスを設定します。

自分のGoogle Driveを読み込めるるように設定します。認証の設定が出てくるので、自身が使っているGmailアドレスを選んで許可してください。そこに出てくる認証データを張り付けてください。

```python
from google.colab import drive
drive.mount('/content/drive')

import sys
ROOT_PATH = 'drive/My Drive/pys_mdr/'
sys.path.append(ROOT_PATH)

```
