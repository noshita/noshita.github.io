Title: 幾何学的形態測定学における二つの流派（２）：標識点に基づく手法
Date: 2015-09-04
Tags: morphometrics, geometric morphometrics, landmark
Slug: geomorph_landmark
Author: Koji NOSHITA
Summary: 
Status: draft


今回は，標識点に基づく幾何学的形態測定学（landmark-based geometric morphometrics）について簡単な説明をしよう．

### 標識点に基づく手法

　標識点に基づく手法では，標識点（landmark）と呼ばれる標本間で対応付けることが可能な点の集合として対象のかたちをモデル化する（Fig. 1）．標識点に基づく手法の理論的背景はshape theoryにより数学的にとても綺麗に整理されている．
Shape theoryの基本的なコンセプトは，単純な標識点の集合である計測データから形状（shape）の情報だけを抽出するとデータはKendall形状空間と呼ばれる多様体上に分布する，ということである．
Kendall形状空間は超球面ないしは半超球面となるため，球面上での統計である方向統計学により一貫した統計解析が可能になることが期待されている．


### 輪郭に基づく手法

　輪郭に基づく手法では，興味ある対象の輪郭を閉曲線または閉曲面によりモデル化する．
最も有名な手法は，楕円フーリエ解析と呼ばれる2次元的な輪郭データをフーリエ係数によりパラメタライズするものであろう．
