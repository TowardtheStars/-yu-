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
\newcommand{\abs}[1]{\left|#1\right|}
\newcommand{\measure}[1]{\left<#1\right>}
\newcommand{\cases}[1]{\begin{cases}#1\end{cases}}
\newcommand{\cprob}[2]{\textrm{Prob}\left(#1|#2\right)}
\end{align*}
$$

 # 半导体器件原理

[TOC]

## 第一章 半导体物理基础

### 有效质量

电子平均运动速度 (相当于波包群速度)
$$
\vec v(\vec k)=\nabla_k\omega(\vec k)=\frac1\hbar\cdot\nabla_k(\vec k)
$$
加速度
$$
\vec a=\difrac{\vec v(\vec k)}{t}=\frac1{\hbar^2}\nabla_k
^2E(\vec k)\cdot\difrac{(\hbar\vec k)}{t}=\boldsymbol m^{*-1}\cdot\vec F
$$

定义有效质量张量 $\boldsymbol m^*$ 为倒有效质量张量 $\boldsymbol m^{*-1}$ 的逆, 于是
$$
m^*_{ij}=\hbar^2\left(\pfrac{^2E(\vec k)}{k_i\partial k_j}\right)^{-1}
$$
在导带底和价带顶退化为标量
$$
E(k)=E(k_0)+\left.\difrac{E(k)}{k}\right|_{k=k_0}\cdot k+\frac12\left.\difrac{^2E(k)}{k^2}\right|_{k=k_0}\cdot k^2=E(k_0)+\frac{\hbar^2k^2}{2m_n^*}
$$
其中 $m_n^*=\hbar^2\left(\difrac{^2E}{k^2}\right)_{k_0}^{-1}$.

### 半导体中的基本控制方程

#### 连续性方程

$$
\begin{align}
\pfrac pt&=D_p\pfrac{^2p}{x^2}-\mu_p\mathscr{E}\pfrac px+G-\frac{\Delta p}{\tau_p}\\
\pfrac nt&=D_n\pfrac{^2n}{x^2}+\mu_n\mathscr{E}\pfrac nx+G-\frac{\Delta n}{\tau_n}
\end{align}
$$

#### 泊松方程

$$
\nabla^2\psi=-\frac\rho\varepsilon=-\frac q\varepsilon(p+N_d-n-N_a)
$$

#### 电流方程

$$
\begin{align}
I_p&=qA\left(p\mu_p\mathscr E-D_p\difrac px\right)\\
I_n&=qA\left(n\mu_n\mathscr E+D_n\difrac nx\right)
\end{align}
$$

## 第二章 PN结  