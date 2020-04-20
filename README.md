# cptk2barracuda
Tensorflow saved model to unity barracuda .nn file. (*.cptkから*.nnに変換）

## summary
ML-Agentsで学習したチェックポイント(*.cptk)をUnityBarracudaのニューラルネットワークモデル(*.nn)に変換

## required
* python 3.6
* ML-Agents 0.13.0 --->  注意
* Tensorflow 2.0.0

## example
```
python cptk2barracuda.py -i models/model-1000.cptk -o output.nn
```

## options
* -i プレフィックス。.cptk.data*、.cptk.index、.cptk.metaが同じフォルダ階層にあること
* -o 出力ファイル名

