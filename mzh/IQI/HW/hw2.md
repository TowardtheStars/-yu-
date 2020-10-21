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
\end{align*}
$$


# 第二次作业

### 1. 计算二元对称信道的信道容量.

设二元对称信道的传输矩阵为
$$
\pmatrix{
P_0&P_1\\
P_1&P_0
}
$$


### 2. 空间中存在两组正交归一化态 $\left\{\ket{\psi_i}\right\}$、 $\left\{\ket{\widetilde\psi_i}\right\}$, 则存在幺正变换 $U$, 使得 $U\ket{\psi_i}=\ket{\widetilde\psi_i}$, 试构造出该 $U$ 变换.



### 3. 空间 $\H$ 中存在两组归一化态$\left\{\ket{\psi_i}\right\}$、 $\left\{\ket{\widetilde\psi_i}\right\}$, 它们满足 $\forall i,j,\braket{\psi_i}{\psi_j}=\braket{\widetilde\psi_i}{\widetilde\psi_j}$. 试证明 $\exist U,\,U\ket{\psi_i}=\ket{\widetilde\psi_i}$, 并构造出该变换.



### 4. 对两比特态 $\ket\varphi=\frac1{\sqrt2}\ket0_A\left(\frac12\ket0_B+\frac{\sqrt3}2\ket1_B\right)+\frac1{\sqrt2}\ket0_A\left(\frac{\sqrt3}2\ket0_B+\frac12\ket1_B\right)$. 
#### (i) 求约化密度矩阵$\rho_A$, $\rho_B$.
#### (ii) 求 $\ket\varphi$ 的 *Schmidt* 分解形式.



### 5. 对三粒子系统纯态$\ket{\varphi_{ABC}}$，在空间 $\H_A\otimes\H_B\otimes\H_C$ 中是否存在 $\H_A$, $\H_B$, $\H_C$ 中的正交基 $\left\{\ket{i_A}\right\}$, $\left\{\ket{i_B}\right\}$, $\left\{\ket{i_C}\right\}$, 使得 $\ket{\varphi_{ABC}}=\sum_I{\sqrt{p_i}\ket{i_A}\otimes\ket{i_B}\otimes\ket{i_C}}$ 一定成立? 给出理由.



### 6. 设 $\ket\psi$ 为量子比特态，在 *Bloch* 球面上均匀随机分布. 

#### (i) 随机地猜想一个态 $\ket\varphi$，求猜测态相对于 $\ket\psi$ 的平均保真度 $\bar F=<\abs{\braket\varphi\psi}^2>$.

#### (ii) 对此量子态做正交测量 $\left\{P_\uparrow,P_\downarrow\right\}$, 其中 $P_\uparrow+P_\downarrow=I$. 测量后系统被制备到: $\rho$, 求 $\rho$ 与原来的态 $\ket\psi$ 的平均保真度 $\bar F=<\bra\psi\rho\ket\psi>$.



### 7. $\ket{\psi_1}=\ket0$, $\ket{\psi_2}=-\frac12\ket0+\frac{\sqrt3}2\ket1$, $\ket{\psi_3}=-\frac12\ket0-\frac{\sqrt3}2\ket1$. 现令 $F_i=\frac23\ketbra{\psi_i}{\psi_i}$，则 $\left\{F_a\right\}_{a=1,2,3}$ 构成二维空间中的 *POVM*. 现引入一个辅助的 *qubit*, 试在扩展空间中实施一个正交测量, 从而实现此 *POVM*.



### 8\*. 证明超算符仅在幺正条件下才是可逆的.