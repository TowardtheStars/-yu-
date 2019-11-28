# 2 量子通讯

[TOC]

## 2.1 量子态的克隆

### 2.1.1 量子态不可克隆定理

### 2.1.2 有限态集合中的不可克隆定理

### 2.1.3 有限态集上的概率克隆

### 2.1.4 量子态的识别



## 2.2 量子密码方案

量子密钥分配: **Q**uantum **K**ey **D**istribution.

### 2.2.1 保密通讯

### 2.2.2 EPR QKD

1. Alice 制备EPR序列, 将其中 B 粒子发给 Bob;
2. Alice, Bob 独立随机地用 Z, X 测量所有的EPR对，保留测量结果;
3. Alice, Bob 公开通讯，Alice 告诉 Bob 测量基，但保密测量结果, Bob保留与Alice选择相同测量基的情况, 告诉Alice，测量的结果形成密钥，同时抛弃他们选择不同测量基的结果;
4. Alice, Bob 随机选择部分测量结果比较，确定是否有人窃听.

### 2.2.3 BB84 QKD

对比 n 比特信息, 发现错误的概率
$$
P_d=1-\left(\frac34\right)^n
$$

### 2.2.4 B92 QKD



### 2.2.5 基于正交态的量子密码方案

### 2.2.6 关于 QKD 的安全性



## 2.3 量子隐形传态

### 2.3.1 相关问题

量子密码: 通过量子通道, 建立经典信息关联

量子态的传送: 通过 EPR 对 + 经典通信

- 仅靠EPR对

  ...

- 仅靠经典通信

  ...

### 2.3.2 Quantum teleportation

Alice 拥有未知量子态 $\left|\psi\right>_C=a\left|0\right>_C+b\left|1\right>_C$

Alice, Bob 共享 Bell 态 $\left|\Phi^+\right>_{AB}$

于是有
$$
\left|\psi\right>_C\left|\Phi^+\right>_{AB}
=\frac12\left|\Phi^+\right>_{CA}\left|\psi\right>_B
+\frac12\left|\Psi^+\right>_{CA}X\left|\psi\right>_B
+\frac12\left|\Psi^-\right>_{CA}ZX\left|\psi\right>_B
+\frac12\left|\Phi^-\right>_{CA}Z\left|\psi\right>_B
$$
通过执行

>CNOT(C,A)
>H(C)

把 $\mathcal H_C\otimes\mathcal H_A$ 的基矢变换到 Bell 基
$$
\begin{equation}
\begin{aligned}
\left|\Phi^+\right>&\rightarrow \left|00\right>\\
\left|\Psi^+\right>&\rightarrow \left|01\right>\\
\left|\Phi^-\right>&\rightarrow \left|10\right>\\
\left|\Psi^-\right>&\rightarrow \left|11\right>\\
\end{aligned}
\end{equation}
$$
然后 Alice 对自己的两个比特进行测量, 则 Bob 的量子态将坍缩到四种情况之一, 根据测量结果进行相应变换即可得到 $\left|\psi\right>$.

### 2.3.3 Dense coding



###  2.3.4 纠缠的 Teleportation 和纠缠交换



### 2.3.5 高维 Hilbert 空间的 Teleportation

