# SimpleCodec

一个极简版本的codec

## 结构定义
encoder：
* enc_start
    * yuv文件读取
    * config文件分析
    * 写pic_head码流
* enc_core
    * 编码器内核
        * fetch
        * rmd (next version)
        * me (next version)
        * md
            * 块划分
                * NS
                * QT
                * else（next version）
            * ipred
                * 横向
                * 竖向
                * planar
                * 角度模式（next version）
            * inter pred（next version）
            * 变换
                * dct2
                * dct8
                * dst7 （next version）
                * else （next version）
            * 量化
                * quant
                * rdoq（next version）
                * else （next version）
        * dbk (next version)
        * sao (next version)
        * else loop filter（next version）
        * aec(无上下文模型）/cabac（包含上下文更新，next version）
* enc_end
    * 写pic_end码流
    * 输出重构
    * 输出码流

**类定义**
* PicInfo（根据config文件得到的各种参数配置信息，后续向下逐级分发）
    * PicWidth、PicHeight、TotalFrame
    * Yorg、Uorg、Vorg
    * else config info（next version）
    * ReadYuv（）
    * ParseCfg（）

* EncCore（encoder内核，存储各类模式信息）
    * 


## Milestone
### 第一阶段版本
1. 支持最大yuv尺寸为1920*1080
2. 实现简易熵编码功能，目标编解码一致，对语法元素只进行二值化处理
3. encoder内核只做块划分，不进行rdo
4. 块划分只支持QT，luma尺寸支持(8x8--32x32), chroma(4x4--16x16)

**码流结构**
1. 包含pic头信息和配置信息
第一阶段版本只需包含pic宽高以及帧数信息，后续加入不同的配置开关信息
2. 包含所有的块划分信息、模式信息以及残差信息
3. 包含码流结束符号位

**Todo**
1. 实现yuv420数据的读取以及组合(done)
2. 实现aec模块，能够对语法元素进行二值化，并能够解码(done)
3. 实现块划分功能，所有LCU强制四叉树划分

