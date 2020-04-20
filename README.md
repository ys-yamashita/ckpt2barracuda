# cptk2barracuda
Tensorflow saved model to unity barracuda .nn file. (*.ckptから*.nnに変換）

## summary
ML-Agentsで学習した*.ckptをUnityBarracudaの*.nnに変換

## required
* python 3.6
* ML-Agents 0.13.0
* Tensorflow 2.0.0

## example
```
python cptk2barracuda.py -i model-1000.cptk -o output.nn
```

## options
* -i 入力フォルダ。checkpoint、model-STEP.cptk.data*、model-STEP.cptk.index、model-STEP.cptk.metaが含まれている必要あり
* -o 出力ファイル名

