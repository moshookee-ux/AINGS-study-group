# 5.5 Q、K、V：完整计算一次注意力

[AINGS](../../README.md) · [多模态多组学](../README.md) · [本模块目录](README.md)

**注意力**让每个词元根据当前内容，从一组其他词元中汇总信息。暂时省略批次轴，输入 $T\in\mathbb R^{L\times d}$ 包含 $L$ 个词元，每行宽度为 $d$。用三个可学习矩阵得到

$$
Q=TW_Q\in\mathbb R^{L\times d_k},\quad
K=TW_K\in\mathbb R^{L\times d_k},\quad
V=TW_V\in\mathbb R^{L\times d_v}.
$$

**查询（Query）**说明当前词元怎样寻找信息；**键（Key）**参与匹配；**值（Value）**提供最终被汇总的内容。$Q$ 和 $K$ 必须具有相同的最后一维，以便计算点积。缩放点积注意力为

$$
S=\frac{QK^{\mathsf T}}{\sqrt{d_k}}+B,\qquad
A=\operatorname{softmax}_{\mathrm{row}}(S),\qquad O=AV.
$$

$S$ 和 $A$ 都是 $L\times L$。第 $i$ 行是第 $i$ 个查询对所有键的分数和权重，softmax 沿每行归一化；$O$ 为 $L\times d_v$，保留查询的数量。$B$ 是加性掩码：允许读取的位置为 0，禁止位置可设为 $-\infty$，对应指数为零。每个有效查询需要至少一个允许位置，才能正常归一化。[R4](https://arxiv.org/abs/1706.03762)

取一个可逐项核对的例子：

$$
T=\begin{bmatrix}1&0\\0&1\end{bmatrix},\quad
W_Q=\begin{bmatrix}1\\0\end{bmatrix},\quad
W_K=\begin{bmatrix}\log3\\0\end{bmatrix},\quad
W_V=\begin{bmatrix}2&0\\0&4\end{bmatrix}.
$$

由矩阵乘法得到 $Q=(1,0)^{\mathsf T}$、$K=(\log3,0)^{\mathsf T}$、$V=\begin{bmatrix}2&0\\0&4\end{bmatrix}$。此时 $d_k=1$，缩放因子为 1，且先令 $B=0$：

$$
S=\begin{bmatrix}\log3&0\\0&0\end{bmatrix},\quad
A=\begin{bmatrix}3/4&1/4\\1/2&1/2\end{bmatrix},\quad
O=\begin{bmatrix}1.5&1\\1&2\end{bmatrix}.
$$

第一行把两个值按 3∶1 汇总，得到 $\frac34(2,0)+\frac14(0,4)=(1.5,1)$；第二行平均汇总。若第一行只能读取第一个键，掩码把它的第二个分数改为 $-\infty$，权重变成 $(1,0)$，输出就变成 $(2,0)$。

除以 $\sqrt{d_k}$ 的理由也可以从统计看：若查询和键的各分量近似独立、均值为零、方差为 1，它们点积的方差随 $d_k$ 增长。缩放可缓和分数随维度扩大而变得过大、softmax 过度集中的现象。实际数据无需严格满足这一假设，这提供了缩放的设计直觉。

注意力权重决定这一层如何组合信息。预测还会经过值投影、多头融合、残差及后续网络，权重大小需要放在完整计算路径中解释。把它联系到生物学调控关系时，还需要额外的证据和验证。

---

[上一篇：5.4 生物词元与嵌入：身份和数值怎样进入网络](04_生物词元与嵌入_身份和数值怎样进入网络.md) · [下一篇：5.6 自注意力、交叉注意力与多头结构](06_自注意力_交叉注意力与多头结构.md)
