统计物理部分
====

[TOC]

## 第六章 近独粒子最概然分布

### 粒子运动状态的经典描述和量子描述

- 线性谐振子
  $$
  \begin{aligned}
  &\varepsilon = \frac{p^2}{2m}+\frac12m\omega^2x^2\\
&\varepsilon_n=\hbar\omega\left(n+\frac12\right),\qquad n=0,1,2,\cdots
  \end{aligned}
  $$
  
- 转子
  $$
  \begin{aligned}
  &\varepsilon = \frac1{2I}\left(p_\theta^2+\frac1{\sin^2\theta}p_\phi^2\right)\\
  &\varepsilon = \frac{p_\phi^2}{2I}=\frac{L^2}{2I},\qquad \mathrm{where}\ \theta = \pi/2\\
  &\varepsilon_l=\frac{l(l+1)\hbar^2}{2I},\qquad l=0,1,2,\cdots
  \end{aligned}
  $$

- 自由粒子
  $$
  \begin{aligned}
  &\varepsilon = \frac1{2m}\left(p_x^2+p_y^2+p_z^2\right)\\
  &p_i=\frac{2\pi\hbar}{L}n_i,\qquad i=x,y,z;\ n_i=0,\pm1,\pm2,\cdots\\
  &\varepsilon_{n_x,n_y,n_z}=\frac{2\pi^2\hbar^2}{m}\frac{n_x^2+n_y^2+n_z^2}{L^2}
  \end{aligned}
  $$
  
  - 量子态数
  
  $$
  \mathrm{d}n_x\mathrm{d}n_y\mathrm{d}n_z=g\left(\frac{L}{2\pi\hbar}\right)^3\mathrm{d}p_x\mathrm{d}p_y\mathrm{d}p_z=g\frac{V}{h^3}\mathrm{d}p_x\mathrm{d}p_y\mathrm{d}p_z
  $$

### 微观状态数

- 量子统计
  $$
  \begin{aligned}
  \Omega_{M.B.}&=\frac{N!}{\prod_l{a_l!}}\prod_l{\omega_l^{a_l}}\\
  \Omega_{B.E.}&=\prod_l{\frac{(\omega_l+a_l-1)!}{a_l!(\omega_l-1)!}}\\
  \Omega_{F.D.}&=\prod_l{\frac{\omega_l!}{a_l!(\omega_l-a_l)!}}
  \end{aligned}
  $$

- 经典统计
  $$
  \Omega_{cl}=\frac{N!}{\prod_l{a_l!}}\prod_l{\left(\frac{\Delta\omega_l}{h_0^r}\right)^{a_l}}
  $$

&emsp;&emsp;经典极限条件（也称非简并条件）下，有
$$
\frac{a_l}{\omega_l}\ll1
\Leftrightarrow
e^\alpha=\frac{V}{N}\left(\frac{2\pi mkT}{h^2}\right)^{3/2}\gg1
\Leftrightarrow 
n\lambda^3=\frac NV\left(\frac{h^2}{2\pi mkT}\right)^{3/2}\ll1\\
\Omega_{B.E.}\approx\frac{\Omega_{M.B.}}{N!}\approx\Omega_{F.D.}
$$

### 最概然分布

&emsp;&emsp;使 $\ln\Omega$ 极大，$\delta\ln\Omega=0$，并且满足约束条件. 可用Lagrange乘子法求解.
$$
\begin{aligned}
\delta N &= \sum_l{\delta a_l}=0\\
\delta E &= \sum_l{\varepsilon_l\delta a_l}=0
\end{aligned}
$$

- 玻尔兹曼分布
  $$
  \begin{aligned}
  &a_l=\omega_le^{-\alpha-\beta\varepsilon_l} & 量子统计\\
  &a_l=e^{-\alpha-\beta\varepsilon_l}\frac{\Delta\omega_l}{h_0^r} & 经典统计
  \end{aligned}
  $$
  
  - $\Delta\omega_l/h_0^r$ 与量子统计中的简并度相当
  
- 玻色（费米）分布
  
  - $\mathrm{def}\ \zeta=
    \left\{\begin{array}{lr}
    {1}&{玻色}\\
    {-1}&{费米}
    \end{array}\right.\\$
  
  $$
  a_l=\frac{\omega_l}{e^{\alpha+\beta\varepsilon_l}- \zeta}
  $$

## 第七章 玻尔兹曼统计

- 最概然分布
  $$
  a_l=\omega_le^{-\alpha-\beta\varepsilon_l}
  $$

### 热力学量的统计表达式

- 单粒子配分函数
  $$
  Z_1:=\sum_l\omega_le^{-\beta\varepsilon_l}
  $$

- 粒子数
  $$
  N=\sum_l{a_l}=e^{-\alpha}Z_1
  $$

- 内能
  $$
  U=\sum_l{\varepsilon_la_l}=-N\frac{\partial}{\partial\beta}\ln Z_1
  $$

- 广义力
  $$
  Y=\sum_l{\frac{\partial \varepsilon_l}{\partial y}a_l}=-\frac{N}{\beta}\frac{\partial}{\partial y}\ln Z_1
  $$

  - 压强
    $$
    p=\frac{N}{\beta}\frac{\partial}{\partial V}\ln Z_1
    $$
  
- 熵
  $$
  S=Nk\left(\ln Z_1-\beta\frac{\partial}{\partial\beta}\ln Z_1\right)\textcolor{red}{-k\ln N!}
  $$

- 自由能
  $$
  F=U-TS=-NkT\ln Z_1\textcolor{red}{+kT\ln N!}
  $$
  
- 经典统计的配分函数
$$
Z_1=\sum_l{e^{-\beta\varepsilon_l}\frac{\Delta\omega_l}{h_0^r}}\\
  Z_1=\int\cdots\int e^{-\beta\varepsilon(p,q)}\frac{\mathrm{d}q_1\mathrm{d}q_2\cdots\mathrm{d}q_r\mathrm{d}p_1\mathrm{d}p_2\cdots\mathrm{d}p_r}{h_0^r}
$$

  

### 能量均分定理

&emsp;&emsp;对于处在温度为T的平衡状态的经典系统，粒子能量中每一个平方项的平均值等于$\frac12kT$.




## 第八章 玻色统计与费米统计

- 最概然分布
  $$
  a_l=\frac{\omega_l}{e^{\alpha+\beta\varepsilon_l}- \zeta}
  $$

### 热力学量的统计表达式

- 巨配分函数
  $$
  \Xi:=\prod_l\Xi_l=\prod_l(1-\zeta e^{-\alpha-\beta\varepsilon_l})^{-\zeta\omega_l}\\
  \ln\Xi=-\sum_l{\zeta\omega_l\ln(1-\zeta e^{-\alpha-\beta\varepsilon_l})}
  $$

- 平均粒子数
  $$
  \overline{N}=\sum_l{a_l}=-\frac{\partial}{\partial\alpha}\ln\Xi
  $$

- 内能
  $$
  U=\sum_l{\varepsilon_la_l}=-\frac{\partial}{\partial\beta}\ln\Xi
  $$

- 广义力

  $$
  Y=\sum_l{\frac{\partial \varepsilon_l}{\partial y}a_l}=-\frac1\beta\frac{\partial}{\partial y}\ln\Xi
  $$

  - 压强
    $$
    p=\frac1\beta\frac{\partial}{\partial V}\ln\Xi
    $$
    

- Lagrange乘子
  $$
  \beta=\frac1{kT},\quad\alpha=-\frac\mu{kT}
  $$

- 熵
  $$
  \begin{aligned}
  S&=k\left(\ln \Xi-\alpha\frac{\partial}{\partial\alpha}\ln\Xi-\beta\frac{\partial}{\partial\beta}\ln\Xi\right)\\
  &=k(ln\Xi+\alpha\overline N+\beta U)
  \end{aligned}
  $$

- 巨热力势
  $$
  J=U-TS-\mu\overline N=-kT\ln\Xi
  $$
  

## 第九章 系综理论

### 微正则系综

$N,V,E$ 守恒

### 正则系综

$N,V,T$ 守恒

#### 正则分布

- 分布函数
  $$
  \begin{aligned}
  \rho_s&=\frac1Ze^{-\beta E_s} &处于态s的概率\\
  \rho_l&=\frac1Z\Omega_le^{-\beta E_l}& 处于能级E_l的概率
  \end{aligned}
  $$

- 配分函数
  $$
  Z=\sum_s{e^{-\beta E_s}}=\sum_l{\Omega_le^{-\beta E_s}}
  $$

- 经典表达式
  $$
  \rho(q,p)\mathrm{d}\Omega=\frac1{N!\ h^{Nr}}\frac{e^{-\beta E(q,p)}}{Z}\mathrm{d}\Omega
  $$
  其中配分函数
  $$
  Z=\frac1{N!\ h^{Nr}}\int{e^{-\beta E(q,p)}\mathrm{d}\Omega}=\frac1{N!\ h^{Nr}}\int\cdots\int e^{-\beta E}\mathrm{d}q_1\mathrm{d}q_2\cdots\mathrm{d}q_{Nr}\mathrm{d}p_1\mathrm{d}p_2\cdots\mathrm{d}p_{Nr}
  $$

#### 热力学公式

- 内能
  $$
  U=\overline E=\frac1Z\sum_s{E_se^{-\beta E_s}}=-\frac{\partial}{\partial\beta}\ln Z
  $$

- 广义力
  $$
  Y=\frac1Z\sum_s{\frac{\partial E_s}{\partial y}e^{-\beta E_s}}=-\frac1\beta\frac{\partial}{\partial y}\ln Z
  $$
  

  - 压强

    $$
    p=\frac1\beta\frac{\partial}{\partial V}\ln Z
    $$

- 熵

  $$
  \begin{aligned}
  S&=k\left(\ln Z-\beta\frac{\partial}{\partial\beta}\ln\Xi\right)\\
  &=k(ln Z+\beta U)
  \end{aligned}
  $$

- 自由能
  $$
  F=U-TS=-kT\ln Z
  $$

### 巨正则系综

$\mu,V,T$ 守恒

#### 巨正则分布

- 分布函数
  $$
  \rho_{Ns}=\frac1\Xi e^{-\alpha N-\beta E_s}
  $$
  
- 配分函数
  $$
  Z=\sum_{N=0}^{\infty}\sum_s{e^{-\alpha N-\beta E_s}}
  $$

- 经典表达式
  $$
  \rho_N\mathrm{d}\Omega=\frac1{N!\ h^{Nr}}\frac{e^{-\alpha N-\beta E(q,p)}}{\Xi}\mathrm{d}\Omega
  $$
  其中配分函数
  $$
  Z=\sum_N\frac{e^{-\alpha N}}{N!\ h^{Nr}}\int{e^{-\beta E(q,p)}\mathrm{d}\Omega}
  $$

#### 热力学公式

- 粒子数
  $$
  \overline N=\frac1\Xi\sum_N\sum_s{Ne^{-\alpha N-\beta E_s}}=-\frac{\partial}{\partial\alpha}\ln\Xi
  $$

- 内能
  $$
  U=\overline E=\frac1\Xi\sum_N\sum_s{E_se^{-\alpha N-\beta E_s}}=-\frac{\partial}{\partial\beta}\ln Z
  $$

- 广义力
  $$
  Y=\frac1\Xi\sum_N\sum_s{\frac{\partial E_s}{\partial y}e^{-\alpha N-\beta E_s}}=-\frac1\beta\frac{\partial}{\partial y}\ln\Xi
  $$
  

  - 压强

    $$
    p=\frac1\beta\frac{\partial}{\partial V}\ln\Xi
    $$

- Lagrange乘子
$$
  \beta=\frac1{kT},\quad\alpha=-\frac\mu{kT}
$$

- 平均场近似

$$
Z_N=[Z_1]^N
$$

- 熵
  $$
  \begin{aligned}
  S&=k\left(\ln \Xi-\alpha\frac{\partial}{\partial\alpha}\ln\Xi-\beta\frac{\partial}{\partial\beta}\ln\Xi\right)\\
  &=k(ln\Xi+\alpha\overline N+\beta U)
  \end{aligned}
  $$

- 巨热力势
  $$
  J=U-TS-\mu\overline N=-kT\ln\Xi
  $$

#### 粒子数涨落

&emsp;&emsp;粒子数的涨落为
$$
\overline{(N-\overline N)^2}=\overline{N^2}-(\overline{N})^2
$$
&emsp;&emsp;而
$$
\frac{\partial \overline N}{\partial\alpha}=\frac{\partial}{\partial\alpha}\frac{\sum_N\sum_s{Ne^{-\alpha N-\beta E_s}}}{\sum_N\sum_s{e^{-\alpha N-\beta E_s}}}=-[\overline{N^2}-(\overline{N})^2]
$$
&emsp;&emsp;于是
$$
\overline{(N-\overline N)^2}=-\left(\frac{\partial \overline N}{\partial\alpha}\right)_{\beta,y}=kT\left(\frac{\partial \overline N}{\partial\mu}\right)_{T,V}\\
\frac{\overline{(N-\overline N)^2}}{(\overline N)^2}=\frac{kT}{(\overline N)^2}\left(\frac{\partial \overline N}{\partial\mu}\right)_{T,V}
$$
&emsp;&emsp;要注意此处的 $\mu$ 为一个粒子的化学势. 利用 $\mathrm{d}\mu=v\mathrm{d}p-s\mathrm{d}T$ 可将相对涨落用易测的量表示
$$
\frac{\overline{(N-\overline N)^2}}{(\overline N)^2}=-\frac{kT}{V^2}\left(\frac{\partial V}{\partial p}\right)_{T,\overline N}=\frac{kT}{V^2}\kappa_T
$$

#### 应用

##### 吸附现象

&emsp;&emsp;$N$个分子在$N_0$个吸附中心上有 $\binom{N_0}{N}$ 个不同的排列，被吸附分子能量为$-\varepsilon_0$.则被吸附分子构成的系统的巨配分函数（注意 $\alpha=-\beta\mu$）
$$
\Xi=\sum_{N=0}^{N_0}{\binom{N_0}{N}e^{\beta(\mu+\varepsilon_0)N}}=\left[1+e^{\beta(\mu+\varepsilon_0)}\right]^{N_0}
$$
&emsp;&emsp;平均分子数
$$
\overline N=-\frac{\partial}{\partial\alpha}\ln\Xi=kT\frac{\partial}{\partial\mu}\ln\Xi=\frac{N_0}{1+e^{-\beta(\mu+\varepsilon_0)}}
$$
&emsp;&emsp;平衡时化学势$\mu$和温度$T$与气体相等
$$
e^{\mu/kT}=e^\alpha=\frac{p}{kT}\left(\frac{h^2}{2\pi mkT}\right)^{3/2}
$$
&emsp;&emsp;于是平衡时吸附率
$$
\theta=\frac{\overline N}{N_0}=\frac1{1+\frac{kT}{p}\left(\frac{2\pi mkT}{h^2}\right)^{3/2}e^{-\varepsilon_0/kT}}
$$

##### 导出近独立粒子平均分布

&emsp;&emsp;讨论普遍情形，即存在简并的情况. 首先引入两个公式
$$
\begin{aligned}
&(1+x)^m=\sum_{n=0}^m{\binom{m}{n}x^n}\\
&(1-x)^{-m}=\sum_{n=0}^\infty{\binom{m+n-1}{n}x^n}\\
\end{aligned}
$$
&emsp;&emsp;将对粒子数 $N$ 和状态 $s$ 的求和变换为对所有可能的分布 $\{a_l\}$ 求和，应乘以分布对应的微观状态数 $\Omega$.
$$
\begin{aligned}
\Xi	&=\sum_N\sum_s{E_se^{-\alpha N-\beta E_s}}=\sum_{\{a_l\}}\Omega e^{-\sum_l(\alpha+\beta\varepsilon_l)a_l}\\
	&=\sum_{\{a_l\}}\prod_l\Omega_l e^{-(\alpha+\beta\varepsilon_l)a_l}\\
	&=\prod_l\sum_{a_l}\Omega_l e^{-(\alpha+\beta\varepsilon_l)a_l}\\
	&=\prod_l\Xi_l
\end{aligned}
$$
&emsp;&emsp;其中 $\Xi_l=\sum_{a_l}\Omega_l e^{-(\alpha+\beta\varepsilon_l)a_l}$

&emsp;&emsp;分布可由下式求得
$$
\overline{a_l}=-\frac{\partial}{\partial\alpha}\ln\Xi_l
$$

- 玻尔兹曼分布
  $$
  \begin{aligned}
  \Omega_l&=\frac{\omega_l^{a_l}}{a_l!}\\
  \therefore \Xi_l&=\sum_{a_l=0}^\infty{\frac{\omega_l^{a_l}}{a_l!}e^{-(\alpha+\beta\varepsilon_l)a_l}}\\
  &=\sum_{a_l=0}^\infty{\frac{1}{a_l!}\left[\omega_le^{-(\alpha+\beta\varepsilon_l)}\right]^{a_l}}\\
  &=\exp\left[\omega_le^{-(\alpha+\beta\varepsilon_l)}\right]\\
  \therefore \ln\Xi_l&=\omega_le^{-\alpha-\beta\varepsilon_l}\\
  \therefore  \overline{a_l}&=-\frac{\partial}{\partial\alpha}\ln\Xi_l=\omega_le^{-\alpha-\beta\varepsilon_l}
  \end{aligned}
  $$
  

- 玻色分布
  $$
  \begin{aligned}
  \Omega_l&=\binom{\omega_l+a_l-1}{a_l}\\
  \therefore \Xi_l&=\sum_{a_l=0}^\infty{\binom{\omega_l+a_l-1}{a_l}e^{-(\alpha+\beta\varepsilon_l)a_l}}\\
  &=\left[1-e^{-(\alpha+\beta\varepsilon_l)}\right]^{-\omega_l}\\
  \therefore \ln\Xi_l&=-\omega_l\ln\left[1-e^{-(\alpha+\beta\varepsilon_l)}\right]\\
  \therefore  \overline{a_l}&=-\frac{\partial}{\partial\alpha}\ln\Xi_l=\frac{\omega_l}{e^{\alpha+\beta\varepsilon_l}- 1}
  \end{aligned}
  $$
  

- 费米分布
  $$
  \begin{aligned}
  \Omega_l&=\binom{\omega_l}{a_l}\\
  \therefore \Xi_l&=\sum_{a_l=0}^{\omega_l}{\binom{\omega_l}{a_l}e^{-(\alpha+\beta\varepsilon_l)a_l}}\\
  &=\left[1+e^{-(\alpha+\beta\varepsilon_l)}\right]^{\omega_l}\\
  \therefore \ln\Xi_l&=\omega_l\ln\left[1+e^{-(\alpha+\beta\varepsilon_l)}\right]\\
  \therefore  \overline{a_l}&=-\frac{\partial}{\partial\alpha}\ln\Xi_l=\frac{\omega_l}{e^{\alpha+\beta\varepsilon_l}+ 1}
  \end{aligned}
  $$

##### 各种分布的涨落

$$
\overline{(a_l-\overline {a_l})^2}=-\frac{\partial \overline {a_l}}{\partial\alpha}=
\left\{\begin{array}{ll}
\overline{a_l}&玻尔兹曼分布\\
\overline{a_l}\left(1+\zeta\frac{\overline{a_l}}{\omega_l}\right)&玻色(费米)分布
\end{array}\right.
$$



## 附录

### 常用积分

$$
\int_{-\infty}^{\infty}{e^{-a x^2}\mathrm{d}x}=\sqrt{\frac\pi a}
$$

