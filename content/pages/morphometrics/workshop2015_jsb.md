Title: 育種学会2015秋　若手の会ワークショップ
Date: 2015-09-20 18:00
Modified: 2015-09-20 18:00
Tags: 研究
Slug: workshop2015_jsb
Authors: Koji NOSHITA
Bibliography: pages/morphometrics/workshop2015_jsb.bib
Summary: 育種学会2015秋の若手の会ワークショップでおこなった葉の輪郭形状解析のまとめ

## 葉の輪郭形状解析
@(Chitwood2012)を例に，葉の輪郭形状解析からどのような生物学的・農学的知見が明らかにできるかをみていく．



## 使うツールやデータ

### [Fiji](http://fiji.sc/Fiji)
[ImageJ](http://imagej.nih.gov/ij/)の生命科学系プラグインのバンドル版．

#### インストール


### R

### データ
ワークショップではChitwood LabのWebページで公開している　の画像データベースのサンプルを利用した．
本データは@(Chitwood2012)の解析に実際に用いられたデータセットである．
しかし，著作権の関係でここにそれらデータを転載することはしない．
興味がある方は[Chitwood Lab](http://www.chitwoodlab.org/)のDatabaseのページを参照されたい．


代わりに，野下がその辺りの草むらで採取した　の葉の画像データを例に解析を進める．


## 楕円フーリエ解析

### 楕円フーリエ解析でできること
「左右成分」の分離は@(Iwata1998)を参照．



## 解析手順

画像をFijiに読み込み解析を開始しよう．

### 領域分割（Fiji）

Fijiには幾つかの領域分割のための機能がある．
もっと単純な　と　によるLevel Setsによる領域分割を紹介する．



これらの他にもFijiには領域分割のためのプラグインが複数ある．
「Plugin」→「Segmentation」で利用できるので試してみて欲しい．

### 二値化（Fiji）


### エッヂ検出（Fiji）

### エッヂ検出（Momocs）

### 楕円フーリエ解析（Momocs）

### 主成分分析（Momocs）

### 形状の再構築（Momocs）



## 参考文献

[REFERENCES]


## リンク

* [育種学と農学のこれからを考える30 〜フェノタイピングは頭痛の種？〜](https://sites.google.com/a/ut-biomet.org/jsb-2015autumn-workshop/)
* [育種学会（第128回講演会）@新潟大学](http://www.nacos.com/jsb/06/06gaiyou.html)
* [育種学会](http://www.nacos.com/jsb/)


