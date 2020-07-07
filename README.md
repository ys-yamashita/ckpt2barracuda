# ckpt2barracuda
Tensorflow saved model to unity barracuda .nn file. (*.ckptから*.nnに変換）

## summary
ML-Agentsで学習したチェックポイント(*.ckpt)をUnityBarracudaのニューラルネットワークモデル(*.nn)に変換

## required
* ubuntu 18.04
* python 3.6
* ML-Agents 0.13.0と0.16.1で動作確認済み 
* Tensorflow 2.0.0と2.1.0で動作確認済み

## example
```
python cptk2barracuda.py -i model/model-1000.ckpt -o output.nn
```

## options
* -i プレフィックス。ファイルパス(*.ckpt) .ckpt.data*、.ckpt.index、.ckpt.metaが同じフォルダ階層にあること
* -o 出力ファイル名(*.nn)

## licence
MIT
