# 1 量子信息和量子计算基础

[TOC]

## 1.1 经典信息论简介

略

## 1.2 量子力学基本假设

### 1.2.1 量子态: 叠加原理

### 1.2.2 力学量: 厄米算符

- 又称可观测量, Observable.
- 厄米矩阵 $A=A^\dagger$.

### 1.2.3 量子态的演化: Schrodinger方程, 幺正演化

- 孤立系统

  - Schrodinger 方程
    $$
    i\hbar\partial_t\left|\varphi\right>=\hat H\left|\varphi\right>
    $$

  - 幺正演化

    若$H$不显含$t$, 则
    $$
    \left|\varphi(t)\right>=U\left|\varphi(0)\right>, \,\mathrm{where}\,U=\exp(iHt/\hbar)
    $$
    此时 $UU^\dagger=U^\dagger U=I$.

### 1.2.4 测量假设: 测量投影假设

- 投影算子
  $$
  P_n=\left|n\right>\left<n\right|
  $$
  $\left|n\right>$ 为力学量本征值 n 相应的本征基矢.

- 详见1.5.1


## 1.3 量子比特及其操作



## 1.4 混合量子态和Schmidt分解

### 1.4.1 混合态: 描述复合系统的子系统



### 1.4.2 密度矩阵的特征



### 1.4.3 Schmidt 分解定理



### 1.4.4 GHJW (Gisin-Hughstom-Josza-Wooters) 定理

- 混合态纯化	

  任何一个 $A$ 空间的密度算符 $\rho_A$, 总可以找到一个扩展空间 $B$ 的纯态, 满足 
  $$
  \rho_A=Tr_B\left(\left|\psi\right>_{AB}\left<\psi\right|\right)
  $$

  扩展纯态的形式不唯一. 

- GHJW 定理

  同一个密度算符的任意两个纯化态之间相差一个扩展空间的幺正变换.



## 1.5 广义测量和演化

### 1.5.1 正交测量: Von Neumann 测量

- 对纯态 $\left|\psi\right>=\sum_n{\alpha_n\left|n\right>}$

  以概率
  $$
  \mathrm{Prob}(n)=\left<\psi\right|P_n\left|\psi\right>=\left|\left<n|\psi\right>\right|^2=|\alpha_n|^2
  $$
  坍缩为 $\left|n\right>$.

  表示为混合态系综形式
  $$
  \rho_{out}=\sum_nP_n\left|\psi\right>\left<\psi\right|P_n=\sum_n{|\alpha_n|^2\left|n\right>\left<n\right|}.
  $$


- 对密度矩阵形式 $\rho$

  以概率
  $$
  \mathrm{Prob}(n)=\mathrm{Tr}(P_n\rho)
  $$
  坍缩为
  $$
  \rho_{out}'=\frac{P_n\rho P_n}{Tr(P_n\rho)}.
  $$
  表示为混合态系综形式
  $$
  \rho_{out}''=\sum_nP_n\rho P_n.
  $$

### 1.5.2 广义测量: POVM测量

扩展空间中的正交测量，在子空间中对应正算符值的测量 ( **P**ositive-**O**perator **V**alued **M**easure )，也称广义测量

### 1.5.3 Neumark 定理

任何由n个一维算符组成的广义测量，总可以用扩展 Hilbert空间中的正交测量来实现

### 1.5.4 直积空间中的正交测量

设Hilbert空间 $\mathcal H_A$ 维数为 N, 该空间的一个POVM由测量算符$\{F_a\}, a=1,2,...,n$ 确定,

则扩展空间 $\mathcal H_B$ 维数 $r\ge n/N$

由 Newmark 定理, 可以扩展为
$$
\left|u_a\right>=\left|\tilde\psi_a\right>+\left|\tilde\psi_a^\bot\right>=\left|\tilde\psi_a\right>+\bigoplus_{\mu=1}^{r-1}{\left|\tilde\psi_{\mu,a}^\bot\right>},
$$
且满足 
$$
\left<u_a|u_b\right>=\left<\tilde\psi_a|\tilde\psi_b\right>+\sum_{\mu=1}^{r-1}{\left<\tilde\psi_{\mu,a}^\bot|\tilde\psi_{\mu,b}^\bot\right>=\delta_{ab}}.
$$
于是能得到 $\mathcal H_A\otimes\mathcal H_B$ 空间下的一组正交基
$$
\left|\Phi_a\right>_{AB}=\left|\tilde\psi_a\right>_A\left|0\right>_B+\sum_{\mu=1}^{r-1}{\left|\tilde\psi_{\mu,a}^\bot\right>}_A\left|\mu\right>_B,\, a=1,2,...,n.
$$

### 1.5.5 超算符

#### 算符和表示

- 算符和表示
  $$
  \begin{equation}
  \begin{aligned}
  $(\rho_A)
&=\rho_A' \\
  &= \mathrm{Tr}_B\left( U_{AB}(\rho_A\otimes\left|0\right>_B\sideset{_B}{}
  {\left<0\right|})U_{AB}^\dagger \right)\\
  &=\sum_\mu{ \sideset{_B}{_B}{\left<\mu|U_{AB}|0\right>} \rho_A \sideset{_B}{_B}{\left<0|U_{AB}|\mu\right>}}\\
  &=\sum_\mu{M_\mu\rho_A M_\mu^\dagger}\\
  \end{aligned}
  \end{equation}
  $$
  其中 $M_\mu=\left<\mu|_BU_{AB}|0\right>_B$.
  
- 给定一个算符和表示，可以创造一个相应的幺正表示.

- 给定一个超算符后，其算符和表示不唯一
  $$
  $(\rho_A)=\sum_\mu{M_\mu\rho_A M_\mu^\dagger}=\sum_\nu{N_\nu\rho_A N_\nu^\dagger},
  $$
  其中 $N_\nu=U_{\nu\mu}M_\mu$.

### 1.5.6 Kraus表示理论

任何满足以下条件的超算符总可以写成算符和的形式

- 线性性
- 保厄米
- 保迹性
- 正定性

### 1.5.7 子系统的动力学演化: 主方程

我猜不考



## 1.6 EPR佯谬, Bell不等式, CHSH不等式



## 1.7 量子纠缠简介

### 1.7.1 纠缠的定义和特性

#### 定义

- 纯态: 不能表示成两个或者多个子系统的直积形式; 对于两体, Schmidt分解项数大于1.
- 混合态: 可分态和纠缠态.

#### 特性

**LOCC** 下纠缠不能增加.

- **LO**: **L**ocal **O**peration, 包括局域的POVM和广义演化.

- **CC**: **C**lassical **C**ommunication, 经典通讯.

### 1.7.2 纠缠的度量

#### 两体复合系统的纠缠度量

- 生成纠缠 (entanglement of formation)

  通过 LOCC 过程, 制备目标状态所消耗的 Bell 基的平均最小数目.

  Alice 和 Bob 先共享 Bell 基, 假设制备出$\rho_{AB}$, 若制备${\rho_{AB}}^{\otimes n}$需要 $k$ 个 Bell 基，则生成纠缠
  $$
  E_F=\lim_{n\rightarrow\infty}{\frac{k_{min}}n}
  $$

- 蒸馏纠缠(entanglement of distillation)

  通过 LOCC 过程, 可以从目标纠缠态中提取的最大 Bell 基数目

  若有 n 个 $\rho_{AB}$, 可以提取 $k'$ 个 Bell 基，则蒸馏纠缠
  $$
  E_D=\lim_{n\rightarrow\infty}{\frac{k'_{max}}n}
  $$

#### Concurrence

译为并发度 or 共生.
$$
\begin{equation}
\begin{gathered}
\tilde\rho=(\sigma_y\otimes\sigma_y)\rho^*(\sigma_y\otimes\sigma_y)\\
R=\sqrt{\sqrt\rho\tilde\rho\sqrt\rho},\,\mathrm{whose \,eigenvalue\,is\,}\lambda_1\ge\lambda_2\ge\lambda_3\ge\lambda_4\\
C(\rho)=max\{0,\lambda_1-\lambda_2-\lambda_3-\lambda_4\}
\end{gathered}
\end{equation}
$$
生成纠缠: 
$$
E_F(\rho)=h\left( \frac{1+\sqrt{1-C(\rho)^2}}2 \right),
$$

其中 $h(x)=-x\log_2 x-(1-x)\log_2(1-x)$.

#### 相对熵

$$
S(\sigma||\rho)=\mathrm{Tr}\left( \sigma(\log_2\sigma-\log_2\rho) \right).
$$

### 1.7.3 纠缠态的判定和分类

#### Peres-Horodecki 判据

若两体密度矩阵可分，则其部分转置矩阵仍为半正定的密度矩阵

- 部分转置半正定：PPT, Positive Partial Transpose
- 判定两体系统可分的必要条件.
- 对于2x2,2x3系统，P-H判据为可分态的充要条件.



## 1.8 量子信息论简介

### 1.8.1 Von Neumann熵

#### 定义

$$
S(\rho)=-\mathrm{Tr}(\rho\log\rho)=-\sum_i{\lambda_i\log\lambda_i}
$$

#### 性质

- Purity

  $S(\rho)=0$ 当且仅当 $\rho$ 表示纯态

- Invariance
  $$
  S(U\rho U^{-1})=S(\rho),\, \mathrm{where}\, U\, \mathrm{is\, unitary}
  $$

- Maximum
  $$
  S(\rho)\le \log D
  $$

- Concavity

  $$
  S(\lambda_1\rho_1+\cdots+\lambda_n\rho_n)\ge\lambda_1S(\rho_1)+\cdots+\lambda_nS(\rho_n)
  $$
  其中 $\lambda_i>0, \sum{\lambda_i}=1$.

- Entropy of measurement
  $$
  H(Y)\ge S(\rho),\,\mathrm{where}\, Y=\{a_y,p(a_y)=\left<a_y\right|\rho\left|a_y\right>\}
  $$
  当且仅当 $[\rho,A]=0$ 即力学量与密度矩阵对易时取等号.

- Entropy of preparation
  $$
  H(X)\ge S(\rho),\,\mathrm{where}\, \rho=\sum_x{p_x\left|\varphi_x\right>\left<\varphi_x\right|}
  $$
  当且仅当 $\{\left|\varphi_x\right>\}$ 为一组正交基时取等号.

-  次加性
  $$
  S(\rho_{AB})\le S(\rho_A)+S(\rho_B)
  $$

-  强次加性
  $$
  S(\rho_{ABC})+S(\rho_B)\le S(\rho_{AB})+S(\rho_{BC})
  $$

- 三角不等式
  $$
  \left|S(\rho_A)-S(\rho_B)\right|\le S(\rho_{AB})\le S(\rho_A)+S(\rho_B)
  $$
  

### 1.8.2 可提取信息与 Holevo 极限定理

- Holevo信息
  $$
  \chi(\xi)=S(\rho)-\sum_x{p_xS(\rho_x)}
  $$

### 1.8.3 量子信源编码定理



### 1.8.4 噪声信道的经典信息容量



---

Typed by MZH