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
\end{align*}
$$

# 第一次作业

### 1. 给定事件集合 $X=\{x_1,x_2,\ldots,x_n\}$ 及相应的概率 $P=\{p_1,p_2,\ldots,p_n\}$ ，证明该事件集的联合熵满足 $H(X)\le log_2(n)$

**证明** 
$$
\begin{equation}
\begin{aligned}
H(X)-log_2n&=\sum_i{p_iI(x_i)}+\sum_i{p_i\log_2\frac1n}\\
&=\sum_ip_i\log_2\frac1{np_i}\\
&\le\sum_i{\frac{p_i}{\ln2}(\frac1{np_i}-1)}\\
&=\sum_i{\frac1{\ln2}\left(\frac1n-p_i\right)}=0
\end{aligned}
\end{equation}
$$
得证.

其中不等式由 $\forall x>0, \ln x\le x-1$ 给出, 下证之.

当 $x>0$ 时, 对于 $f(x)=lnx-(x-1)$, 有 $f'(x)=1/x-1$, $f''(x)=-1/x^2<0$ .

故 $f(x)$ 在 $f'(x)=0$ (即 $x=1$) 处取到极大值 0.

从而 $f(x)\le 0$, 即 $\ln x\le x-1$.

证毕.



### 2. 对任意给定的事件集 $X_1$, $X_2$ 及系数 $0\le a\le1$ ，证明香农熵的上凸性，即 $aH(X_1)+(1−a)H(X_2)≤H\left[aX_1+(1−a)X_2\right]$

**证明**
$$
\begin{equation}
\begin{aligned}
H\left[aX_1+(1-a)X_2\right]&=-\sum_i{\left[ap_i^{(1)}+(1-a)p_i^{(2)}\right]\log_2\left[ap_i^{(1)}+(1-a)p_i^{(2)}\right]}\\
&=-a\sum_ip_i^{(1)}\log_2\left[p_i^{(1)}\frac{ap_i^{(1)}+(1-a)p_i^{(2)}}{p_i^{(1)}}\right]\\
&-(1-a)\sum_ip_i^{(2)}\log_2\left[p_i^{(2)}\frac{ap_i^{(1)}+(1-a)p_i^{(2)}}{p_i^{(2)}}\right]\\
&=aH(X_1)+(1-a)H(X_2)-\left\{a\sum_ip_i^{(1)}\log_2\left[\frac{ap_i^{(1)}+(1-a)p_i^{(2)}}{p_i^{(1)}}\right]\\
+(1-a)\sum_ip_i^{(2)}\log_2\left[\frac{ap_i^{(1)}+(1-a)p_i^{(2)}}{p_i^{(2)}}\right]\right\}
\end{aligned}
\end{equation}
$$
而我们有
$$
\begin{equation}
\begin{aligned}
\sum_i{ p_i^{(1)}\log_2\left[\frac{ap_i^{(1)}+(1-a)p_i^{(2)}}{p_i^{(1)}}\right] }
&\le\sum_i{ \frac{p_i^{(1)}}{\ln2}\left[\frac{ap_i^{(1)}+(1-a)p_i^{(2)}}{p_i^{(1)}}-1\right] }\\
&=\frac{1-a}{\ln2}\sum_i{ \left(p_i^{(2)}-p_i^{(1)}\right) }=0\\

\sum_ip_i^{(2)}\log_2\left[\frac{ap_i^{(1)}+(1-a)p_i^{(2)}}{p_i^{(2)}}\right] &\le\sum_i{ \frac{p_i^{(2)}}{\ln2}\left[\frac{ap_i^{(1)}+(1-a)p_i^{(2)}}{p_i^{(2)}}-1\right] }\\
&=\frac{a}{\ln2}\sum_i{ \left(p_i^{(1)}-p_i^{(2)}\right) }=0
\end{aligned}
\end{equation}
$$
又由于 $a\ge0, 1-a\ge0$ , 故 (2) 式右边大括号中的项小于等于0, 从而
$$
aH(X_1)+(1−a)H(X_2)≤H\left[aX_1+(1−a)X_2\right]
$$
证毕.




### 3. 证明联合熵的链式法则: $H(X_1X_2\ldots X_N)=H(X_1)+H(X_2|X_1)+\ldots+H(X_N|(X_1X_2\ldots X_{N−1}))$

**证明**
$$
H(X_1X_2\ldots X_N)=\sum_{i_1i_2\ldots i_N}{ p(x_{i_1}x_{i_2}\ldots x_{i_N})\log_2p(x_{i_1}x_{i_2}\ldots x_{i_N}) }
$$
其中
$$
p(x_{i_1}x_{i_2}\ldots x_{i_N})= \prod_{k=1}^{N}{ p(x_{i_k}|x_{i1}x_{i_2}\ldots x_{i_{k-1}}) }
$$
于是
$$
\begin{equation}
\begin{aligned}
H(X_1X_2\ldots X_N)&=-\sum_{i_1i_2\ldots i_N}
\left[
	p(x_{i_1}x_{i_2}\ldots x_{i_N})
	\log_2	\prod_{k=1}^{N}
	{ 
		p(x_{i_k}|x_{i_1}x_{i_2}\ldots x_{i_{k-1}}) 
	} 
\right]\\

&=-\sum_{k=1}^N
\left[
    \sum_{i_1i_2\ldots i_N}
        p(x_{i_1}x_{i_2}\ldots x_{i_N}) 
        \log_2p(x_{i_k}|x_{i_1}x_{i_2}\ldots x_{i_{k-1}}) 
\right]
\\

&=-\sum_{k=1}^N
\left\{
    \sum_{i_1i_2\ldots i_k}
    \left[
        \sum_{i_{k+1}i_{k+2}\ldots i_{N}}
            p(x_{i_{k+1}}x_{i_{k+2}}\ldots x_{i_N}|x_{i_1}x_{i_2}\ldots x_{i_k})\\
            p(x_{i_1}x_{i_2}\ldots x_{i_k}) 
            \log_2p(x_{i_k}|x_{i_1}x_{i_2}\ldots x_{i_{k-1}}) 
    \right]
\right\}
\\
\end{aligned}
\end{equation}
$$

由于
$$
\sum_{i_{k+1}i_{k+2}\ldots i_{N}}
	p(x_{i_{k+1}}x_{i_{k+2}}\ldots x_{i_N}|x_{i_1}x_{i_2}\ldots x_{i_k})=1
$$
从而 (7) 式化为
$$
\begin{equation}
\begin{aligned}
H(X_1X_2\ldots X_N)&=-\sum_{k=1}^N
\left[
    \sum_{i_1i_2\ldots i_k}
        p(x_{i_1}x_{i_2}\ldots x_{i_k}) 
        \log_2p(x_{i_k}|x_{i_1}x_{i_2}\ldots x_{i_{k-1}})
\right]
\\

&=\sum_{k=1}^N
\left\{
    \sum_{i_1i_2\ldots i_{k-1}}
        p(x_{i_1}x_{i_2}\ldots x_{i_{k-1}})
        \left[
        -\sum_{i_k}
             p(x_{i_k}|x_{i_1}x_{i_2}\ldots x_{i_{k-1}}) 
            \log_2p(x_{i_k}|x_{i_1}x_{i_2}\ldots x_{i_{k-1}}) 
        \right]
\right\}
\\

&=\sum_{k=1}^N
\left[
    \sum_{i_1i_2\ldots i_{k-1}}
        p(x_{i_1}x_{i_2}\ldots x_{i_{k-1}})
        H(X_k|x_{i_1}x_{i_2}\ldots x_{i_{k-1}}) 
\right]
\\

&=\sum_{k=1}^N
	H(X_k|X_1X_2\ldots X_{k-1}) 
\\

&= H(X_1)+H(X_2|X_1)+\ldots+H(X_N|(X_1X_2\ldots X_{N−1}))

\end{aligned}
\end{equation}
$$
证毕.




### 4. 复习矩阵上三角化的 *Schur* 定理，并以此为基础论证厄密矩阵的谱分解性质，即任意厄密矩阵 A，总可以幺正对角化成一个实对角矩阵；再把本征向量表示成 Dirac 记号，从而把 A 简单表示讲义上的成 Dirac 记号的形式.

任意复方阵 A 酉相似于上三角阵, 即 $\exist U, T=U^\dagger AU$ 为上三角阵. 则
$$
T^\dagger=(U^\dagger AU)^\dagger=U^\dagger A^\dagger U
$$
若 $A$ 是厄密的, 即 $A=A^\dagger$, 则 $T=T^\dagger$, 于是 $T$ 为实对角阵. 

故对任意厄密矩阵 $A$, 总可以幺正对角化为实对角阵.

记本征向量为 $\ket{\psi_i}$, 相应的本征值为 $\lambda_i (i=1,2,\ldots,n)$, 则
$$
\begin{align}
U&=\left(\ket{\psi_1}, \ket{\psi_1},\ldots,\ket{\psi_n}\right)\\
T&=\mathrm{diag}\left(\lambda_1,\lambda_2,\ldots,\lambda_n\right)
\end{align}
$$
于是 $A$ 可以表示为
$$
A=UU^\dagger AUU^\dagger=UTU^\dagger=\sum_{i=1}^n{\lambda_i\ketbra{\psi_i}{\psi_i}}
$$


