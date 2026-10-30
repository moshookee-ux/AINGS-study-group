# 5.7 前馈网络、残差与归一化：组成一个 Transformer 块

[AINGS](../../README.md) · [多模态多组学](../README.md) · [本模块目录](README.md)

一个 Transformer 块一般包含注意力子层和逐词元前馈子层。**前馈网络（FFN）**对每个词元使用同一套 MLP，例如
$\operatorname{FFN}(h)=\operatorname{ReLU}(hW_1+b_1)W_2+b_2$。若 $h$ 为 $L\times d$，$W_1$ 为 $d\times d_{\mathrm{ff}}$、$W_2$ 为 $d_{\mathrm{ff}}\times d$，FFN 先扩展通道再映射回来。它在此步骤内逐行变换；注意力负责行与行之间的信息交换。

**残差连接**把输入与更新相加：$h'=h+F(h)$。例如原向量为 $(2,1)$、更新为 $(-0.5,0.2)$，结果为 $(1.5,1.2)$。相加两侧需要同形状。残差保留信息与梯度的直接路径，网络可以学习对已有表示做多大修改。

**LayerNorm**通常在一个词元的隐藏通道上计算均值和方差：

$$
\operatorname{LN}(h)_j=\gamma_j\frac{h_j-\bar h}{\sqrt{v_h+\varepsilon}}+\beta_j.
$$

$\gamma_j,\beta_j$ 是可学习的缩放与偏移，$\varepsilon$ 是防止除零的小正数。对 $(1,3)$，均值为 2、方差为 1；忽略极小的 $\varepsilon$，并取 $\gamma=(1,1)$、$\beta=(0,0)$，结果为 $(-1,1)$。它处理隐藏激活的尺度；RNA 总量归一化处理输入测量尺度，二者发生在不同位置。[MATH1](https://arxiv.org/abs/1607.06450)

**RMSNorm**使用均方根缩放：$\operatorname{RMSNorm}(h)_j=\gamma_jh_j/\sqrt{\frac1d\sum_kh_k^2+\varepsilon}$。它省去减均值步骤；对 $(1,3)$，分母约为 $\sqrt5$，输出约为 $(0.447,1.342)$。因此 RMSNorm 与 LayerNorm 对平移的反应不同。[MATH2](https://arxiv.org/abs/1910.07467)

归一化的放置位置形成两种常见结构：

$$
\begin{aligned}
\text{Post-Norm: }&H=\operatorname{Norm}(T+\operatorname{MHA}(T)),\quad
T'=\operatorname{Norm}(H+\operatorname{FFN}(H));\\
\text{Pre-Norm: }&H=T+\operatorname{MHA}(\operatorname{Norm}(T)),\quad
T'=H+\operatorname{FFN}(\operatorname{Norm}(H)).
\end{aligned}
$$

两者都保持词元数量和隐藏宽度；区别在于归一化是否位于残差分支计算之前。这个选择会影响优化和梯度传播，Pre-Norm 堆叠末尾通常还会有最终归一化。实际结构还可能在子层加入 dropout。[R4](https://arxiv.org/abs/1706.03762) [MATH3](https://proceedings.mlr.press/v119/xiong20b.html)

**门控前馈**再增加一个按输入控制的乘法分支。SwiGLU 的一种省略偏置写法是 $[\operatorname{SiLU}(hW_a)\odot(hW_b)]W_o$：两条分支先投影到相同宽度，一条经过激活后调节另一条，再投影回来。这里“门”描述逐通道的调节，与注意力对不同词元加权属于不同计算位置。[MATH4](https://arxiv.org/abs/2002.05202)

---

[上一篇：5.6 自注意力、交叉注意力与多头结构](06_自注意力_交叉注意力与多头结构.md) · [下一篇：5.8 编码器、解码器与生成顺序](08_编码器_解码器与生成顺序.md)
