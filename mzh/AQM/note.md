$$
\begin{align*}
\newcommand{\ket}[1]{\left|{#1}\right>}
\newcommand{\bra}[1]{\left<{#1}\right|}
\newcommand{\braket}[2]{\left<{#1}|{#2}\right>}
\newcommand{\ketbra}[2]{\left|{#1}\right>\left<#2\right|}
\newcommand{\pfrac}[2]{\frac{\partial #1}{\partial #2}}
\newcommand{\difrac}[2]{\frac{\textrm{d}{#1}}{\textrm{d}{#2}}}
\newcommand{\Tr}{\textrm{Tr}}
\newcommand{\T}{\textrm{T}}
\newcommand{\H}{\mathcal{H}}
\newcommand{\abs}[1]{\left|#1\right|}
\newcommand{\measure}[1]{\left<#1\right>}
\newcommand{\cases}[1]{\begin{cases}#1\end{cases}}
\newcommand{\cprob}[2]{\textrm{Prob}\left(#1|#2\right)}
\newcommand{\prob}[1]{\textrm{Prob}\left(#1\right)}
\newcommand{\mleq}[1]{\begin{equation}\begin{aligned}#1\end{aligned}\end{equation}}
\newcommand{\commute}[2]{\left[#1,#2\right]}
\end{align*}
$$

# 高量笔记

[TOC]
## 第一章
### 1.1 SG 实验

电子自旋角动量 $\vec S$ 是量子化的, 自旋磁矩 $\vec\mu = -g_S\mu_B\vec S/\hbar$ . 于是电子在磁场 $\vec B$ 中发生偏转, 且偏转是分立的

角动量 $\vec S$ 的各个分量不能同时测定

要描述 $\vec S$, 可以类比偏振光的数学描述: 即复矢量

### 1.2 右矢, 左矢和算符

零元, 幺元, 逆元, 加法交换, 加法结合, 数乘结合, 数乘分配(数), 数乘分配(矢量) $\Longrightarrow$ 矢量空间

+内积(交换共轭, 分配, 结合, 半正定) $\Longrightarrow$ 内积空间

+空间完备性 $\Longrightarrow$ Hilbert空间

### 1.6 位置, 动量和平移

正则对易关系
$$
\commute{x_i}{x_j}=\commute{p_i}{p_j}=0,\qquad
\commute{x_i}{p_j}=i\hbar\delta_{ij}
$$
有用的公式
$$
\begin{align}
\commute{x_i}{F(\boldsymbol p)}&=i\hbar\pfrac{F}{p_i}\\
\commute{p_i}{G(\boldsymbol x)}&=-i\hbar\pfrac{G}{x_i}
\end{align}
$$




## 第二章

### 薛定谔绘景和海森伯绘景

态右矢的薛定谔方程
$$
i\hbar\pfrac{}t\ket{\alpha,t_0;t}_S=H\ket{\alpha,t_0;t}_S
$$
海森伯运动方程
$$
\difrac{A^{(H)}}t=\frac1{i\hbar}\left[A^{(H)},H\right]
$$
