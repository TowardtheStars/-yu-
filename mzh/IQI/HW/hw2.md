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
# 第二次作业


### 1. 计算二元对称信道的信道容量.

设信源为 A, 经过信道后的信息为 B. 并令
$$
 \prob{A=0}=p_0,\quad \prob{A=1}=p_1
$$
其中 $p_0+p_1=1$.

则信源 A 的信息熵
$$
H(A)=-p_0\log_2p_0-p_1\log_2p_1.
$$
设二元对称信道的传输矩阵为
$$
\pmatrix{
P_0&P_1\\
P_1&P_0
}
$$
其中 $P_0+P_1=1$.

则信源 A 的条件熵
$$
\begin{equation}
\begin{aligned}
H(A|B)=&-\prob{A=0}\cprob{B=0}{A=0}\log_2\cprob{A=0}{B=0}\\
&-\prob{A=0}\cprob{B=1}{A=0}\log_2\cprob{A=0}{B=1}\\
&-\prob{A=1}\cprob{B=0}{A=1}\log_2\cprob{A=1}{B=0}\\
&-\prob{A=1}\cprob{B=1}{A=1}\log_2\cprob{A=1}{B=1}\\
=&-p_0P_0\log_2P_0-p_0P_1\log_2P_1-p_1P_1\log_2P_1-p_1P_0\log_2P_0\\
=&-P_0\log_2P_0-P_1\log_2P_1
\end{aligned}
\end{equation}
$$
于是信道传输率
$$
R=H(A)-H(A|B)=-p_0\log_2p_0-p_1\log_2p_1+P_0\log_2P_0+P_1\log_2P_1.
$$
我们令 $\pfrac{R}{p_0}=0$, 解得 $p_0=p_1=\frac12$. 易验证此时 R 取到极大值.

故信道容量
$$
C=\max_{\{p_0,p_1\}}R=1+P_0\log_2P_0+P_1\log_2P_1
$$


### 2. 空间中存在两组正交归一化态 $\left\{\ket{\psi_i}\right\}$、 $\left\{\ket{\widetilde\psi_i}\right\}$, 则存在幺正变换 $U$, 使得 $U\ket{\psi_i}=\ket{\widetilde\psi_i}$, 试构造出该 $U$ 变换.

令
$$
U=\sum_i{\ketbra{\widetilde\psi_i}{\psi_i}}
$$
则有
$$
\begin{equation}
\begin{aligned}
U\ket{\psi_i}
&=\sum_k{
	\ketbra{\widetilde\psi_k}{\psi_k}\cdot\ket{\psi_i}
}\\

&=\sum_k{
	\braket{\psi_k}{\psi_i}\cdot\ket{\widetilde\psi_k}
}\\

&=\sum_k{
	\delta_{ki}\ket{\widetilde\psi_k}
}\\

&=\ket{\widetilde\psi_i}
\end{aligned}
\end{equation}
$$
下证 $U$ 是酉的,
$$
\begin{equation}
\begin{aligned}
U^\dagger U
&=\sum_i{
	\ketbra{\psi_i}{\widetilde\psi_i}
}
\cdot\sum_j{
	\ketbra{\widetilde\psi_j}{\psi_j}
}\\

&=\sum_{ij}{
	\ket{\psi_i}\braket{\widetilde\psi_i}{\widetilde\psi_j}\bra{\psi_j}
}\\

&=\sum_{ij}{
	\ket{\psi_i}\delta_{ij}\bra{\psi_j}
}\\

&=\sum_i{
	\ket{\psi_i}\bra{\psi_i}
}\\

&=I
\end{aligned}
\end{equation}
$$
得证.



### 3. 空间 $\H$ 中存在两组归一化态$\left\{\ket{\psi_i}\right\}$、 $\left\{\ket{\widetilde\psi_i}\right\}$, 它们满足 $\forall i,j,\braket{\psi_i}{\psi_j}=\braket{\widetilde\psi_i}{\widetilde\psi_j}$. 试证明 $\exist U,\,U\ket{\psi_i}=\ket{\widetilde\psi_i}$, 并构造出该变换.

对 $\left\{\ket{\psi_i}\right\}$、 $\left\{\ket{\widetilde\psi_i}\right\}$ 分别做 *Schmidt* 正交化, 得
$$
\begin{cases}
\ket{\psi_i}=\sum_j{A_{ij}\ket j},&\braket ij=\delta_{ij}\\
\ket{\widetilde\psi_i}=\sum_j{\widetilde A_{ij}\ket {\widetilde j}},&\braket{\widetilde i}{\widetilde j}=\delta_{ij}\\
\end{cases}
$$
于是有
$$
\begin{equation}
\begin{aligned}
\braket{\psi_i}{\psi_j}
&=\sum_k{
{A_{ik}^*\bra k}
}
\cdot\sum_j{
{A_{jl}^*\ket l}
}\\

&=\sum_{kl}{
	A_{ik}^*A_{jl}^*\braket kl
}\\

&=\sum_{kl}{
	A_{ik}^*A_{jl}^*\delta_{kl}
}\\

&=\sum_{k}{
	A_{ik}^*A_{jk}
}
\end{aligned}
\end{equation}
$$
同理有
$$
\braket{\widetilde\psi_i}{\widetilde\psi_j}=\sum_{k}{
	\widetilde A_{ik}^*\widetilde A_{jk}
}
$$
于是有 $\forall i,j$,
$$
\sum_{k}{
	A_{ik}^*A_{jk}
}
=\braket{\psi_i}{\psi_j}
=\braket{\widetilde\psi_i}{\widetilde\psi_j}
=\sum_{k}{
	\widetilde A_{ik}^*\widetilde A_{jk}
}.
$$
显然我们可以取 $\widetilde A=A$ 来实现 *Schmidt* 正交化.

由题 2 知, 我们可以构造酉变换 $U=\sum_i\ketbra{\widetilde i}i$ 使得 $U\ket i=\ket{\widetilde i}$.

此时有
$$
U\ket{\psi_i}=U\sum_j{A_{ij}\ket j}=\sum_j{A_{ij}U\ket j}=\sum_j{\widetilde A_{ij}\ket{\widetilde j}}=\ket{\widetilde\psi_i}
$$
至此, 我们已经构造出了满足条件的酉变换 $U$.



### 4. 对两比特态 $\ket\varphi=\frac1{\sqrt2}\ket0_A\left(\frac12\ket0_B+\frac{\sqrt3}2\ket1_B\right)+\frac1{\sqrt2}\ket1_A\left(\frac{\sqrt3}2\ket0_B+\frac12\ket1_B\right)$. 
#### (i) 求约化密度矩阵$\rho_A$, $\rho_B$.

对空间 $\H_A$ 求部分迹, 得
$$
\begin{equation}
\begin{aligned}
\rho_A
&=\Tr_B\ketbra\varphi\varphi\\
&=\sideset{_B}{_B}{\bra0\cdot\ketbra\varphi\varphi\cdot\ket0}+\sideset{_B}{_B}{\bra1\cdot\ketbra\varphi\varphi\cdot\ket1}\\
&=\left(\frac1{2\sqrt2}\ket0_A+\frac{\sqrt3}{2\sqrt2}\ket1_A\right)\left(\frac1{2\sqrt2}\bra0_A+\frac{\sqrt3}{2\sqrt2}\bra1_A\right)\\
&\quad+\left(\frac{\sqrt3}{2\sqrt2}\ket0_A+\frac1{2\sqrt2}\ket1_A\right)\left(\frac{\sqrt3}{2\sqrt2}\bra0_A+\frac1{2\sqrt2}\bra1_A\right)\\
&=\frac12\ket0_A\bra0+\frac{\sqrt3}4\ket0_A\bra1+\frac{\sqrt3}4\ket1_A\bra0+\frac12\ket1_A\bra1\\
&=\pmatrix{
\frac12&\frac{\sqrt3}4\\
\frac{\sqrt3}4&\frac12
}
\end{aligned}
\end{equation}
$$
对 $\H_A$ 空间求部分迹, 得
$$
\begin{equation}
\begin{aligned}
\rho_B
&=\Tr_A\ketbra\varphi\varphi\\
&=\sideset{_A}{_A}{\bra0\cdot\ketbra\varphi\varphi\cdot\ket0}+\sideset{_A}{_A}{\bra1\cdot\ketbra\varphi\varphi\cdot\ket1}\\
&=\left(\frac1{2\sqrt2}\ket0_B+\frac{\sqrt3}{2\sqrt2}\ket1_B\right)\left(\frac1{2\sqrt2}\bra0_B+\frac{\sqrt3}{2\sqrt2}\bra1_B\right)\\
&\quad+\left(\frac{\sqrt3}{2\sqrt2}\ket0_B+\frac1{2\sqrt2}\ket1_B\right)\left(\frac{\sqrt3}{2\sqrt2}\bra0_B+\frac1{2\sqrt2}\bra1_B\right)\\
&=\frac12\ket0_B\bra0+\frac{\sqrt3}4\ket0_B\bra1+\frac{\sqrt3}4\ket1_B\bra0+\frac12\ket1_B\bra1\\
&=\pmatrix{
\frac12&\frac{\sqrt3}4\\
\frac{\sqrt3}4&\frac12
}
\end{aligned}
\end{equation}
$$



#### (ii) 求 $\ket\varphi$ 的 *Schmidt* 分解形式.

令 $\det(\lambda I-\rho_A)=0$, 解得本征矢
$$
\cases{
	\ket{+}_A=\frac1{\sqrt2}\left(\ket0_A+\ket1_A\right),&\lambda_{+}=\frac{2+\sqrt3}4\\
	\ket{-}_A=\frac1{\sqrt2}\left(\ket0_A-\ket1_A\right),&\lambda_{-}=\frac{2-\sqrt3}4
}
$$
令 $\det(\lambda I-\rho_B)=0$, 解得本征矢
$$
\cases{
	\ket{+}_B=\frac1{\sqrt2}\left(\ket0_B+\ket1_B\right),&\lambda_{+}=\frac{2+\sqrt3}4\\
	\ket{-}_B=\frac1{\sqrt2}\left(\ket0_B-\ket1_B\right),&\lambda_{-}=\frac{2-\sqrt3}4
}
$$
现在对 $\H_A, \H_B$ 均有
$$
\cases{
\ket0=\frac1{\sqrt2}\left(\ket++\ket-\right)\\
\ket1=\frac1{\sqrt2}\left(\ket+-\ket-\right)
}
$$
于是
$$
\begin{equation}
\begin{aligned}
\ket\varphi
&=\frac1{\sqrt2}\ket0_A\left(\frac12\ket0_B+\frac{\sqrt3}2\ket1_B\right)+\frac1{\sqrt2}\ket1_A\left(\frac{\sqrt3}2\ket0_B+\frac12\ket1_B\right)\\
&=\frac12\left(\ket+_A+\ket-_A\right)\left(\frac{\sqrt3+1}{2\sqrt2}\ket+_B-\frac{\sqrt3-1}{2\sqrt2}\ket-_B\right)\\
&\quad+\frac12\left(\ket+_A-\ket-_A\right)\left(\frac{\sqrt3+1}{2\sqrt2}\ket+_B+\frac{\sqrt3-1}{2\sqrt2}\ket-_B\right)\\
&=\frac{\sqrt3+1}{2\sqrt2}\ket+_A\ket+_B\quad-\quad\frac{\sqrt3-1}{2\sqrt2}\ket-_A\ket-_B
\end{aligned}
\end{equation}
$$


### 5. 对三粒子系统纯态$\ket{\varphi_{ABC}}$，在空间 $\H_A\otimes\H_B\otimes\H_C$ 中是否存在 $\H_A$, $\H_B$, $\H_C$ 中的正交基 $\left\{\ket{i_A}\right\}$, $\left\{\ket{i_B}\right\}$, $\left\{\ket{i_C}\right\}$, 使得 $\ket{\varphi_{ABC}}=\sum_I{\sqrt{p_i}\ket{i_A}\otimes\ket{i_B}\otimes\ket{i_C}}$ 一定成立? 给出理由.



### 6. 设 $\ket\psi$ 为量子比特态，在 *Bloch* 球面上均匀随机分布. 

#### (i) 随机地猜想一个态 $\ket\varphi$，求猜测态相对于 $\ket\psi$ 的平均保真度 $\bar F=<\abs{\braket\varphi\psi}^2>$.

#### (ii) 对此量子态做正交测量 $\left\{P_\uparrow,P_\downarrow\right\}$, 其中 $P_\uparrow+P_\downarrow=I$. 测量后系统被制备到: $\rho$, 求 $\rho$ 与原来的态 $\ket\psi$ 的平均保真度 $\bar F=<\bra\psi\rho\ket\psi>$.

$$
\frac1{4\pi}\int_0^{2\pi}\mathrm{d}\varphi\int_0^\pi \sin\theta\mathrm{d}\theta=1
$$



### 7. $\ket{\psi_1}=\ket0$, $\ket{\psi_2}=-\frac12\ket0+\frac{\sqrt3}2\ket1$, $\ket{\psi_3}=-\frac12\ket0-\frac{\sqrt3}2\ket1$. 现令 $F_i=\frac23\ketbra{\psi_i}{\psi_i}$，则 $\left\{F_a\right\}_{a=1,2,3}$ 构成二维空间中的 *POVM*. 现引入一个辅助的 *qubit*, 试在扩展空间中实施一个正交测量, 从而实现此 *POVM*.



### 8\*. 证明超算符仅在幺正条件下才是可逆的.