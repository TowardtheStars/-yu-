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
\newcommand{\cases}[1]{\left\{\begin{matrix}#1\end{matrix}\right.}
\newcommand{\cprob}[2]{\textrm{Prob}\left(#1|#2\right)}
\newcommand{\set}[1]{\left\{#1\right\}}
\newcommand{\Row}{\textrm{Row}}
\newcommand{\Col}{\textrm{Col}}
\newcommand{\Null}{\textrm{Null}}
\newcommand{\dim}{\textrm{dim}}
\newcommand{\rank}{\textrm{rank}}
\newcommand{\det}{\textrm{det}}
\begin{equation*}
\end{equation*}
$$

# 量子计算

<http://home.ustc.edu.cn/~mzh/public/IQI/QC.html>

[TOC]

## 1 量子计算复杂度



## 2 量子计算模型I 量子线路模型



## 3 量子计算模型II 绝热量子计算



## 4 量子计算模型III one-way 量子计算



## 5 量子算法I

**一些性质:**
$$
\begin{align}
H^{\bigotimes n}&: \ket x\to\sum_{y=0}^{2^n-1}{\frac{(-1)^{x\cdot y}\ket y}{2^{n/2}}}\\
U_f&: \ket{x, y}\to\ket{x, f(x)\oplus y}\\
&: \ket{x}\otimes\frac{\ket0-\ket1}{\sqrt2}\to (-1)^{f(x)}\ket{x}\otimes\frac{\ket0-\ket1}{\sqrt2}
\end{align}
$$
其中 $x\cdot y=\bigoplus_i{x_i y_i}$. 



### 5.1 D-J 算法

**问题:** 判断 $f:\{0,1\}^n\rightarrow\{0,1\}$是常函数还是平衡函数

- Step 1:
  $$
  H^{\bigotimes(n+1)}:\qquad\ket{0}^{n}\ket1 \rightarrow \sum_{x=0}^{2^n-1}{\frac{\ket x}  {2^{n/2}}}\otimes\frac{\ket0-\ket1}{\sqrt2}
  $$
- Step 2:  
  
  
  $$
  U_f:\qquad \ldots\rightarrow \sum_{x=0}^{2^n-1}{\frac{(-1)^{f(x)}\ket x}  {2^{n/2}}}\otimes\frac{\ket0-\ket1}{\sqrt2}
  $$

- Step 3:
  $$
  H^{\bigotimes n}\otimes I:\qquad\ldots\rightarrow\sum_{y=0}^{2^n-1}\sum_{x=0}^{2^n-1}{\frac{(-1)^{f(x)}(-1)^{x\cdot y}\ket{y}}{2^n}}\otimes\frac{\ket0-\ket1}{\sqrt2}
  $$
  
- Step4: 测量前n个比特

  - 对于常函数, 测得 $\ket y$ 态的概率幅为
    $$
    \sum_{x=0}^{2^n-1}{\frac{(-1)^{f(x)}(-1)^{x\cdot y}}{2^n}}=(-1)^{f(x)}\sum_{x=0}^{2^n-1}{\frac{(-1)^{x\cdot y}}{2^n}}=(-1)^{f(x)}\delta_{y,0}
    $$
    故测量后以概率 1 坍缩到  $\ket0$.

  - 对于平衡函数, 测得 $\ket0$ 态的概率幅为
    $$
    \sum_{x=0}^{2^n-1}{\frac{(-1)^{f(x)}}{2^n}}=0
    $$
    故测量后以概率 0 坍缩到 $\ket0$.
    
    **注:** 此处的 $\ket0$ 是指 $\ket0^{\bigotimes n}$.

### 5.2 Grover 算法



## 6 量子算法II

### 6.1 Simon 算法



### 6.2 QFT 算法



### 6.3 Shor 算法



## 7 物理系统I 线性光学系统



## 8 物理系统II 离子阱



## 9 量子噪声和退相干





## 10 量子纠错码 (QECC)

### 10.1 量子纠错码的构思

基本想法: 多数表决

- 3比特 bit-flip 纠错码
  $$
  \begin{equation}
  \begin{aligned}
  \ket0&\rightarrow\ket{0_L}\equiv\ket{000}\\
  \ket1&\rightarrow\ket{1_L}\equiv\ket{111}
  \end{aligned}
  \end{equation}
  $$

- 3比特 phase-flip 纠错码
  $$
  \begin{equation}
  \begin{aligned}
  \ket0&\rightarrow\ket{0_L}\equiv\ket{+++}\\
  \ket1&\rightarrow\ket{1_L}\equiv\ket{---}
  \end{aligned}
  \end{equation}
  $$

- 9比特 Shor 码
  $$
  \begin{equation}
  \begin{aligned}
  \ket0&\rightarrow\ket{0_L}\equiv\frac{\left(\ket{000}+\ket{111}\right)\left(\ket{000}+\ket{111}\right)\left(\ket{000}+\ket{111}\right)}{2\sqrt2}\\
  \ket1&\rightarrow\ket{1_L}\equiv\frac{\left(\ket{000}-\ket{111}\right)\left(\ket{000}-\ket{111}\right)\left(\ket{000}-\ket{111}\right)}{2\sqrt2}
  \end{aligned}
  \end{equation}
  $$

***定理*** 若一个 QECC 可以纠正错误 $A$ 和错误 $B$, 则它可以纠正错误 $\alpha A+\beta B$.

只需纠正 t 比特上的 Pauli 错误即可纠正 t 比特上的所有错误.



### 10.2 经典编码理论

#### 线性码

*正交补:* <https://zh.wikipedia.org/wiki/%E6%AD%A3%E4%BA%A4%E8%A1%A5>

用 $n$ 比特编码 $k$ 比特的线性码称作 $[n,k]$ 码.

线性码有两种等价表示, 生成矩阵 $G$ 和奇偶检验矩阵 $H$.

$G$ 为 $n\times k$ 矩阵, $H$ 为 $ (n-k)\times n$ 矩阵.

给定 $G$ 和 $H$, 则列空间 $\Col(G)$ 和行空间 $\Row(H)$($\Leftrightarrow\Col(H^T)$) 互为正交补空间, 即 $\Col(G)^\bot=\Row(H)$, 相应的码字集合 $C$ 满足

- $C=\set{Gx|x\in被编码信息}$
- $C=\set{y|Hy=0}$, 即奇偶检验矩阵 $H$ 的零 (核) 空间 $\Null(H)$.

奇偶检验矩阵可用于纠错
$$
Hy'=H(y+e_i)=He_i
$$

#### Hamming 距离

- 码字的 Hamming 权重
  $$
  wt(x)=码字x中非零位数目
  $$
  
- 码字之间的 Hamming 距离
  $$
  d(x,y)=wt(x+y)
  $$
  
- 码字集合的 Hamming 距离
  $$
  d(C)=\min_{x,y\in C, x\ne y}d(x,y)=\min_{x\in C, x\neq0}wt(x)
  $$
  
  QCQI[1] 练习 10.20 告诉我们, 奇偶校验矩阵 $H$ 所定义的码的 Hamming 距离等于 $\rank(H)+1$. 特别的, Hamming 码的距离为 3.

***定理*** Hamming距离至少为 2t+1 的码能纠正最多 t 比特的错误.



### 10.3 CSS 码

#### CSS码的定义

设 $C_1$ 为 $[n,k_1]$ 码, $C_2$为 $[n,k_2]$ 码, 满足$C_2\subset C_1$. 其中 $C_1$ 和 $C_2^\bot$ 能纠 t 比特的错误, 相应的奇偶校验矩阵记作 $H_1$ 和 $H_2$.

则可以定义 $CSS(C_1,C_2)$:
$$
\ket{x+C_2}\equiv\frac1{\sqrt{\abs{C_2}}}\sum_{y\in C_2}\ket{x+y}
$$
其中 $x\in C_1$. 

可以看出 $\ket{x+C_2}$ 取决于陪集 $x+C_2$ (由于是交换群, 也可写成 $C_2+x$).

记 $C_1/C_2=\set{x+C_2|x\in C_1}$, 它的元素个数为 $\abs{C_1}/\abs{C_2}=2^{k_1-k_2}$.

因此 $CSS(C_1,C_2)$ 是个 $[n, k_1-k_2]$ 量子码.

#### 纠错

CSS码最多能纠正 t 比特 bit-flip 和 phase-flip 错误.

将 n 比特噪声信道中的 bit-flip 错误记作 $e_1$, phase-flip 错误记作 $e_2$.

则 $\ket{x+C_2}$ 经过这个噪声信道变为
$$
\frac1{\sqrt{\abs{C_2}}}\sum_{y\in C_2}{(-1)^{(x+y)\cdot e_2}\ket{x+y+e_1}}
$$
引入足量的辅助比特用于存储差错症状, 均初始化为 $\ket0$ 态.

1. bit-flip 纠错
   $$
   C^{\bigotimes n}(H_1):\qquad \ldots\to \frac1{\sqrt{\abs{C_2}}}\sum_{y\in C_2}{(-1)^{(x+y)\cdot e_2}\ket{x+y+e_1}}\otimes\ket{H_1e_1}
   $$
   测量辅助比特即可纠正相应 t 比特错误, 得到
   $$
    \frac1{\sqrt{\abs{C_2}}}\sum_{y\in C_2}{(-1)^{(x+y)\cdot e_2}\ket{x+y}}
   $$

2. phase-flip 纠错
   
   首先应用 H 门, 得到
   $$
   H^{\bigotimes n}:\qquad \ldots\to \frac1{\sqrt{\abs{C_2}2^n}}\sum_z\sum_{y\in C_2}{(-1)^{(x+y)\cdot (e_2+z)}\ket{z}}
   $$
   令 $z'\equiv z+e_2$, 则可重写为
   $$
   \frac1{\sqrt{\abs{C_2}2^n}}\sum_z\sum_{y\in C_2}{(-1)^{(x+y)\cdot z'}\ket{z'+e_2}}
   $$
   当前仅当 $z'\in C_2^\bot$ 时, $\sum_{y\in C_2}(-1)^{y\cdot z'}$ 有非零值 $\abs{C_2}$, 可重写为
   $$
   \frac1{\sqrt{2^n/\abs{C_2}}}\sum_{z'\in C_2^\bot}{(-1)^{x\cdot z'}\ket{z'+e_2}}
   $$
   使用类似 bit-flip 的方式, 引入辅助比特, 应用 $C^{\bigotimes n}(H_2)$ 后纠错, 得到
   $$
   \frac1{\sqrt{2^n/\abs{C_2}}}\sum_{z'\in C_2^\bot}{(-1)^{x\cdot z'}\ket{z'}}
   $$
   再次应用 H 门, 得到
   $$
   \begin{equation}
   \begin{aligned}
   H^{\bigotimes n}:\qquad\ldots&\to\frac1{2^n/\sqrt{\abs{C_2}}}\sum_y\sum_{z'\in C_2^\bot}{(-1)^{(x+y)\cdot z'}\ket{y}}\\
   &\to\frac1{\sqrt{\abs{C_2}}}\sum_{y\in C_2}{\ket{x+y}}
   \end{aligned}
   \end{equation}
   $$

#### 实例: Steane 码





### 10.4 稳定子码 (stabilizer code)



### 10.5 环形码 (toric code)



---

以下内容只在课件开头提纲中提到, 并无具体内容, 应该是没讲到

### 10.6 拓扑量子计算

???

### 10.7 容错量子计算

???

---

\[1\] Nielsen M A, Chuang I L. Quantum Computation and Quantum Information[M]. Cambridge university press, 2010.

---

Typed by MZH