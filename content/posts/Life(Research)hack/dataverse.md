Title: Dataverseから画像データをまとめて取得する
Date: 2015-11-25 19:18:01
Tags: blog,dataverse, database, python
Slug: 00004
Author: Koji NOSHITA
Summary: Dataverseから画像ファイルをpythonを使って無理やりまとめてダウンロードする．
Status: published

## 問題
[Harvard Dataverse](https://dataverse.harvard.edu/)に保存されている  
あるdatasetから画像データを一括で保存しようとしたらサイズ制限のため 
```
***.jpeg (image/jpeg) **** bytes.
***.jpeg (image/jpeg) skipped because the total size of the download bundle exceeded the limit of ** bytes.
***.jpeg (image/jpeg) skipped because the total size of the download bundle exceeded the limit of ** bytes.
...
```
みたいな記述のMANIFEST.TEXを含んだzipファイルがダウンロードされる．  
結果として，数個しか画像データがダウンロード出来ない．  
手動で一個一個ファイルを落とすなんてイヤだ．

## 解決策
画像データそれぞれのurlを取得して，保存する．

## 手順

### 特定のdataverseがもつfileの一覧を取得する

[dataverseのAPI](http://guides.dataverse.org/en/latest/api/index.html)を見ると
[Search API](http://guides.dataverse.org/en/latest/api/search.html)があるらしいので，これに従い取得する． 

とりあえずブラウザで確認したいって人は
```
https://dataverse.harvard.edu/api/search?=q=*&subtree=[dataverseのid]&type=file&key=[APIトークン]
```
でチェック．
[dataverseのid]は欲しいデータをもつdatasetが含まれるdataverseのidを指定する．  
idはdataverseのurlからわかる．
```
https://dataverse.harvard.edu/dataverse/[dataverseのid]
```  


[APIトークン]はHarvard Dataverseにアカウントを作ると，生成できる．  
参照: [Account Creation & Management](http://guides.dataverse.org/en/latest/user/account.html)


今回はcURLで
```console
curl -X GET https://dataverse.harvard.edu/api/search?=q=*\&subtree=[特定のdataverseのid]\&type=file\&key=[APIトークン] > [保存先のファイル名].json
```
のようにしてjsonファイルとして保存する．  
今回はfilelist.jsonとして保存したとして話を進める．

特定のdatasetがもつfileの一覧を取得できたら早いのだが， 
subtreeオプションやfqオプションでは対応できなさそう．  
なので一旦全部ダウンロードしてから適当なfileだけを選び出す． 

### 必要なfileの取捨選択
取得したjsonファイルを読み込んでフィールドの値に応じて必要なfileをフィルタリングする．  
今回はpythonを利用した． 

大体こんな感じ．
```python
import re,json

# fileの情報一覧の読み込み
with open("filelist.json","r") as f:
	filelist = json.load(f)

# 特定のデータセットを指定するパタン
# 今回はDOIで指定する
PTNDOI = re.compile(r"[データセットを指定するDOI]")
# 欲しいfileの種類を指定するパタン
PTNTYPE = re.compile(r"[fileのtype，e.g. 拡張子]")

# 必要なfile一覧の生成
targetlist = []
for item in filelist:
	if PTNDOI.search(item['dataset_citation']) is not None:
		if PTNTYPE.search(item['file_type']) is not None:
			targetlist.append((item['name'],item['url']))
```
[データセットを指定するDOI]や[fileのtype]には適切な正規表現パタンを記述する．  

後でfileをダウンロードするときにファイル名を保持したいので(url,name)を値に持つリストであるtargetlistを作っている．

### データのダウンロード
wgetなどを利用しても良いが，-iオプション利用時に名前を指定する方法がよくわからなかったので引き続きpythonで作業した．  
大体こんな感じ．

```python
import os, urllib.request

# 出力先の指定
OUTPURDIR = [出力先のディレクトリ]

# fileのダウンロード
for item in targetlist:
	outputfilepath = os.path.join(OUTPUTDIR,item[0])
	# 既にファイルが存在する場合は保存しない
	if not os.path.exists(outputfilepath):
		urllib.request.urlretrieve(item[1],outputfilepath)
```

## 今後の課題
以上のように，pythonを使うとDataverseのデータを割と簡単に取得できた．  
しかし，ホントはもっとdataverseのapiを駆使してシンプルに操作すべきだと思う．  
Search APIのfqオプションの働きがよくわからず，例に上がっていたfq=publication_date_s:2015すらうまく機能しなかった．  

また[Data Access API](guides.dataverse.org/en/latest/api/dataaccess.html)も存在するので  
もう少し賢くダウンロード出来たかもしれない．

* dataverseのAPI
	* Search API
	* Data Access API