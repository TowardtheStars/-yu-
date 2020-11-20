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
\end{align*}
$$
# 第 4 次作业

### 1. Alice 和 Bob 选择 B92 方案来建立量子密钥序列。Alice选择两种态: $\ket{\psi_1}=\ket{z_+}$, $\ket{\psi_2}=\ket{x_+}$, 分别以1/2 的概率发送给Bob, Bob分别以 1/2 的几率选择基 $\{\ket{z_+},\ket{z_-}\}$ 和基 $\{\ket{x_+},\ket{x_-}\}$ 对收到的态进行正交测量.

#### (1) 请论述Alice和Bob将遵从怎样的经典通信协议来建立密钥.



#### (2) 假定存在一个窃听者, 该窃听者试图以概率克隆的方式对该密钥建立过程进行攻击. 则下列的几组克隆概率中, 哪几组在理论上是可能的 (括号中第一个数表示成功地克隆出 $\ket{\psi_1}$ 的概率, 第二个数表示成功地克隆出 $\ket{\psi_2}$ 的概率). 并给出证明.

$$
\begin{align*}
(\frac{2-\sqrt2}2,\,&\frac{2-\sqrt2}2), &(1,\,&0.1), &(0.5,\,&0.5), &(0.7,\,&0.7), &(0.9,\,&0.9)
\end{align*}
$$



#### (3) 窃听者如果克隆失败, 他会随机发送 $\ket{\psi_1}$ 或  $\ket{\psi_2}$ 给 Bob (分别以 1/2 的几率). 如窃听者选择以上几组中最优的克隆方案进行攻击, 则作为 Alice 和 Bob, 他们至少要公开对照多少组数据, 均检验无误, 才能确保该密钥的安全性达到 99% 以上?

 

### 2. 给出高维空间量子 teleportation 的数学证明.

 

### 3. 混合纠缠态 $\rho(\lambda)=(1-\lambda)\ketbra{\Psi^-}{\Psi^-}+\frac\lambda 4I\otimes I$.

#### (a) 求标准 teleportation 的保真度, 并且, 当 $\lambda$ 达到多少时, 保真度将优于经典极限? (所谓经典极限是指: A 方随机选择一组测量基进行测量, 并将测量结果通过经典信道通知 B, B 根据 A 的测量结果进行态制备).



#### (b) 计算 $\prob{\boldsymbol n_\uparrow,\boldsymbol m_\uparrow}=\Tr\left[E_A(\boldsymbol n_\uparrow)E_B(\boldsymbol m_\uparrow)\rho(\lambda)\right]$.