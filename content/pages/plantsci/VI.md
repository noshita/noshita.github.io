Title: 植生指数 Vegetation Indeces
Date: 2016-07-14 19:15:08
Modified: 2016-07-14 19:15:16
Tags: 研究
Slug: VI
Summary: 植生指数のリスト

まずは「植生のリモートセンシング」（Box 7.1: pp. 214-215）を参考にする．

## 単純な指数

|         Name        |           Equation          | pros/cons |            ref             |
| :------------------ | :-------------------------- | :-------- | :------------------------- |
| DVI (Difference VI) | $N-R$                       |           | Tucker (1979)              |
| RVI (Ration VI)     | $\frac{N}{R}$               |           | Birth & McVey (1968)       |
| $CI_{590}$          | $\frac{N_{880}}{VIS_{590}}$ |           | Gitelson & Merzlyak (1997) |


## 正規化指標

|          Name         |      Equation     | pros/cons |         ref         |
| :-------------------- | :---------------- | :-------- | :------------------ |
| NDVI (Normalized DVI) | $\frac{N-R}{N+R}$ | test      | Rouse et al. (1974) |
|                       |                   |           |                     |


## マルチチャネル指標
|               Name               |                      Equation                     | pros/cons |          ref           |
| :------------------------------- | :------------------------------------------------ | :-------- | :--------------------- |
| Kauth - Thomas 変換              | LANDSAT7用                                        |           |                        |
| CAI (Cellulose Absorption Index) | $\frac{0.5 \rho_{2000}-\rho_{2000}}{\rho_{2100}}$ |           | Daughtry et al. (2000) |
|                                  |                                                   |           |                        |

## ハイパースペクトル指標
|                  Name                 |                         Equation                        | pros/cons |          ref           |
| :------------------------------------ | :------------------------------------------------------ | :-------- | :--------------------- |
| REP (Red Edge Position)               |                                                         |           | Jago et al. (1999)参照 |
| PRI (Photochemical Reflectance Index) | $\frac{\rho_{570}-\rho_{531}}{\rho_{531} + \rho_{570}}$ |           | Gamon et al. 1992      |
|                                       |                                                         |           |                        |


## 参考文献
