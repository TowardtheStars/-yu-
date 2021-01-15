$$
\newcommand{\ket}[1]{\left|{#1}\right>}
\newcommand{\bra}[1]{\left<{#1}\right|}
\newcommand{\braket}[2]{\left<{#1}|{#2}\right>}
\newcommand{\ketbra}[2]{\left|{#1}\right>\left<#2\right|}
\newcommand{\pfrac}[2]{\frac{\partial #1}{\partial #2}}
\newcommand{\difrac}[2]{\frac{\textrm{d}{#1}}{\textrm{d}{#2}}}
\newcommand{\Tr}{\textrm{Tr}}
\newcommand{\abs}[1]{\left|#1\right|}
\newcommand{\measure}[1]{\left<#1\right>}
\newcommand{\cprob}[2]{\textrm{Prob}\left(#1|#2\right)}
\newcommand{\if}{\textrm{if}}
\begin{equation*}
\end{equation*}
$$

# One-Way 量子计算

[TOC]

## 图态

### 图态的定义

#### 操作性定义

- 给定一个无向图 $G$, 在每个顶点上放置一个量子比特, 并将每个量子比特都制备到量子态 $\ket{+}$.
- 对每条边相连的两个顶点上的量子比特做 $CZ$ 门.
- 这样生成的态称之为图 $G$ 对应的图态 $\ket G$, 它与 $CZ$ 的顺序无关.

#### 算符定义

- 给定一个图 $G$, 在每个顶点上放置一个量子比特. 对每一个顶点 $a$ 定义一个算符:
  $$
  K_a=X_a\prod_{b\in N_a}Z_b
  $$
  其中 $N_a$ 为 $a$ 的邻结点集合.

- 所有算符 $K_a$ 相互对易, 所有算符 $K_a$ 的本征值为 1 的共同本征态, 称之为图 $G$ 对应的图态 $\ket G$.
  
  - 即 $K_a$ 为图态 $\ket G$ 的稳定子.

若定义哈密顿量:
$$
H=-\sum_aK_a
$$
则图态 $\ket G$ 为 $H$ 的基态.

### 图态的性质

#### 约化密度矩阵

- 图态 $\ket G$ 的约化密度矩阵可以通过稳定子群中的元素平均获得:
  $$
  \rho_G^A=\sum_{\sigma\in S_A}\sigma
  $$
  其中 $A$ 是比特集合， $S_A$ 表示以 $A$ 为支集的稳定子集合.

- 完全图对应图态的任意子集的约化密度矩阵均为单位阵.

#### 局域补操作



#### 测量





## One-Way 量子计算



## 附录

### Clifford 算符对易关系

#### 与 Pauli 算符的对易关系

- Pauli 算符
  $$
  \sigma_b\sigma_a\sigma_b=(-1)^{\delta_{ab}}\sigma_a
  $$

- Pauli 算符的平方根
  $$
  \begin{equation}
  \begin{aligned}
  \sqrt{\pm i\sigma_b}\sigma_a\sqrt{\mp i\sigma_b}
  &=e^{\pm i\frac\pi4\sigma_b}\sigma_ae^{\mp i\frac\pi4\sigma_b}\\
  &=\frac12(I\pm i\sigma_b)\sigma_a(I\mp i\sigma_b)\\
  &=\frac12(\sigma_a+\sigma_b\sigma_a\sigma_b\mp i[\sigma_a,\sigma_b])\\
  &=\delta_{ab}\sigma_a\pm\varepsilon_{abc}\sigma_c
  \end{aligned}
  \end{equation}
  $$

- 其他 Clifford 算符

  略



#### 与测量算符的对易关系

测量算符满足
$$
P^{a,\pm}=\frac{I\pm \sigma_a}2
$$

- Pauli算符
  $$
  \sigma_bP^{a,\pm}\sigma_b=\frac{I\pm(-1)^{\delta_{ab}}\sigma_a}2=
  \begin{cases}
  P^{a,\pm}&\if\quad a=b\\
  P^{a,\mp}&\if\quad a\ne b
  \end{cases}
  $$
  
- Pauli算符的平方根
  $$
  \sqrt{\pm_1i\sigma_b}P^{a,\pm_2}\sqrt{\mp_1\sigma_b}=\frac{I\pm_2(\delta_{ab}\sigma_a\pm_1\varepsilon_{abc}\sigma_c)}2=
  \begin{cases}
  P^{a,\pm_2}&\if\quad a=b\\
  P^{c,\pm_2\cdot\pm_1\cdot\varepsilon_{abc}}	& \if \quad (a\ne b)\and (c\ne a)\and (c\ne b)
  \end{cases}
  $$
  

