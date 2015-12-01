Title: 育種学会2015秋　若手の会ワークショップ
Date: 2015-09-20 18:00
Modified: 2015-09-20 18:00
Tags: 研究
Slug: workshop2015_jsb
Authors: Koji NOSHITA
Bibliography: pages/morphometrics/workshop2015_jsb.bib
Summary: 育種学会2015秋の若手の会ワークショップでおこなった葉の輪郭形状解析のまとめ

## 葉の輪郭形状解析
@(Chitwood2012)例に，葉の輪郭形状解析からどのような生物学的・農学的知見が明らかにできるかを紹介しました．  
また，輪郭形状解析によく用いられる楕円フーリエ解析をFijiとRを利用しておこなう手順を例示しました．  
ここでは，FijiとRを利用した楕円フーリエ解析の流れをより具体的に解説します．

## 使うツールやデータ

### [Fiji](http://fiji.sc/Fiji)
[ImageJ](http://imagej.nih.gov/ij/)の生命科学系プラグインのバンドル版．
今回は

* 領域分割
* 二値化
* エッヂ検出

に用います．

参考: 

* インストール方法（[Installation](http://fiji.sc/Installation)）  
* 基本的な使い方（[Tutorials](http://fiji.sc/Category:Tutorials)）
	* [Getting started](http://fiji.sc/Getting_started)
	* [Image Processing Principles](http://fiji.sc/Image_Processing_Principles)
	* [Cookbook](http://fiji.sc/Cookbook)
	* [Using the Script Editor](http://fiji.sc/Using_the_Script_Editor)
* 様々なプラグイン（[Plugins](http://fiji.sc/Category:Plugins)）


### [R](https://www.r-project.org/)
統計解析用プログラミング言語，またはその実装．  
今回ははR及びそのパッケージの[Momocs](https://github.com/vbonhomme/Momocs/)を用いて，

* エッヂ検出
* 楕円フーリエ解析
* 主成分分析
* 形態の再構築

をおこないます．

#### [Momocs](https://github.com/vbonhomme/Momocs/)
主に輪郭形状解析を目的としたRのパッケージ．  
現在も開発中ですので，開発者のGitHubレポジトリから最新版をインストールします．  
GitHubからのインストールにはdevtools([GitHub](https://github.com/hadley/devtools),[CRAN](https://cran.r-project.org/web/packages/devtools/index.html))を利用しますので，

* Windowsでは[Rtools](https://cran.r-project.org/bin/windows/Rtools/)
* Macでは[Xcode](https://developer.apple.com/jp/xcode/downloads/)
* Linuxでは各種コンパイラやライブラリ

がそれぞれ必要となります．

以下では，WindowsとMacでのMomocsのインストールまでの手順を説明します．  
Linuxの方は各自頑張れると思います．


##### Windows

##### Mac

### サンプルデータ
ワークショップではChitwood LabのWebページで公開しているトマトの野生種の画像データベースのサンプルを利用しました．  
これらのデータは@(Chitwood2012)の解析に実際に用いられたデータセットです．  
しかし，著作権的な問題のため，ここにそれらデータを転載することはしません．  
興味がある方は[Chitwood Lab](http://www.chitwoodlab.org/)の[Wild relatives of tomato | Database](http://www.chitwoodlab.org/#!wild-relatives-of-tomato/c1o7b)を参照して下さい．

代わりに，ここでは@(Chitwood2015)のブドウの野生種の葉の画像データの一部を楕円フーリエ解析の具体的な手順の説明に用います．
<!-- **そのため結果として出てくる図は@(Chitwood2012)の知見とは一致しません．**  -->
データは[Harverd Dataverse](https://dataverse.harvard.edu/)にて[CC0](https://creativecommons.org/publicdomain/zero/1.0/)で公開されています．

* [Climate and developmental plasticity: interannual variability in grapevine leaf morphology](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/KOG6SY)

ここでは，このデータセットから10枚の葉の画像を抜き出したサンプルデータを利用します．

## 解析手順

### 準備
サンプルデータとコード一式は[こちら]()からダウンロードできます．  
これを解凍し，作業ディレクトリとします．  
作業ディレクトリは，このような構成になっていると想定します．  

- wsJBS2015Aut
	- data
		* image001.jpg
		* image002.jpg
		* ...
	* fijiSample.ijm
	* rSample.r

作業ディレクトリの構成を維持しておけば，作業ディレクトリ自体はどこに配置しても構いません．

### Fijiでの前処理

画像をFijiに読み込み解析を開始します．  
画像の取り込みはドラッグ&ドロップまたは「File」→「Open...」を選択し行います．

#### 1. 領域分割

Fijiには幾つかの領域分割のためプラグインが導入されています．．  
ここでは，もっと単純な　と　によるLevel Setsによる領域分割を紹介します．



これらの他にもFijiには領域分割のためのプラグインが複数あります．
「Plugin」→「Segmentation」で利用できるので試してみて下さい．

#### 2. 二値化


#### 3. エッヂ検出

### Rでの輪郭形状解析と統計処理

#### 1. エッヂ検出

#### 2. 楕円フーリエ解析

#### 3. 主成分分析

#### 4. 形状の再構築

## もう少し踏み込んだ解析

** 本節は加筆中です．しばらくお待ち下さい．**


楕円フーリエ解析で輪郭形状を定量化・再構築できることがわかりました．  
しかし，それだけで科学的に面白い知見が得られる訳ではありません．  
<!-- 例えば，@(Chitwood2012)では-->
以下では，幾つかのもう少し踏み込んだ解析例を紹介します．



### 輪郭形状の左右成分の分離

詳細は@(Iwata1998)を参照．

### 種間での輪郭形状差の検出

### 左右・遠位-近位での輪郭形状差の検出

### 成長に伴う輪郭形状の変化

### GWASやGSへの応用


<!--
## @(Chitwood2012)における形状解析の再現
繰り返しになりますが，ここでは@(Chitwood2015a)と@(Chitwood2015)のブドウの野生種の葉の画像データを用い，@(Chitwood2012)と同様の解析をおこないます．  
**そのため結果として出てくる図は@(Chitwood2012)の知見とは一致しません．**
あくまで解析のデモと考えて下さい．

### 楕円フーリエ解析による左右成分の分離
「左右成分」の分離の詳細は@(Iwata1998)を参照．
-->


## 参考文献

[REFERENCES]


## リンク

* [育種学と農学のこれからを考える30 〜フェノタイピングは頭痛の種？〜](https://sites.google.com/a/ut-biomet.org/jsb-2015autumn-workshop/)
* [育種学会（第128回講演会）@新潟大学](http://www.nacos.com/jsb/06/06gaiyou.html)
* [育種学会](http://www.nacos.com/jsb/)
