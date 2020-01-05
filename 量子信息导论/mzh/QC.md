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
其中 $x\cdot y$ 为按位与.



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
    故测量后以概率 1 坍缩到  $\ket 0^{\bigotimes n}$.

  - 对于平衡函数, 测得 $\ket0$ 态的概率幅为
    $$
    \sum_{x=0}^{2^n-1}{\frac{(-1)^{f(x)}}{2^n}}=0
    $$
    故测量后以概率 0 坍缩到 $\ket 0^{\bigotimes n}$

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

**定理:** 若一个 QECC 可以纠正错误 $A$ 和错误 $B$, 则它可以纠正错误 $\alpha A+\beta B$.

只需纠正 t 比特上的 Pauli 错误即可纠正 t 比特上的所有错误.



### 10.2 经典编码理论

线性码的奇偶检验矩阵和生成矩阵互为正交补空间

### 10.3 CSS 码



### 10.4 稳定子码 (stabilizer code)



### 10.5 环形码 (toric code)



---

以下内容只在课件开头提纲中提到, 并无具体内容, 应该是没讲到

### 10.6 拓扑量子计算

???

### 10.7 容错量子计算

???

---

Typed by MZH
