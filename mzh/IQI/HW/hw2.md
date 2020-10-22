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

对 $\left\{\ket{\psi_i}\right\}$ 做 *Schmidt* 正交化, 得
$$
\begin{align*}
\ket{0'}&=\ket{\psi_0}\\
\ket{1'}&=\ket{\psi_1}-\frac{\braket{0'}{\psi_1}}{\braket {0'}{0'}}\ket{0'}\\
\ket{2'}&=\ket{\psi_2}-\frac{\braket{0'}{\psi_2}}{\braket {0'}{0'}}\ket{0'}-\frac{\braket{1'}{\psi_2}}{\braket {1'}{1'}}\ket{1'}\\
\cdots\\
\ket{i'}&=\ket{\psi_i}-\sum_{n=0}^{i-1}\frac{\braket{n'}{\psi_i}}{\braket {n'}{n'}}\ket{n'}\\
\end{align*}
$$
并进行归一化 $\ket{i}=\frac{1}{\braket{i'}{i'}}\ket{i'}$, 得到正交归一化态 $\left\{\ket{i}\right\}$.

注意到正交化过程中的系数仅和 $\braket{\psi_i}{\psi_j}$ 相关, 因此我们可以用同样的系数对 $\left\{\ket{\widetilde \psi_i}\right\}$ 做 *Schmidt* 正交化得到 $\left\{\ket{\widetilde i}\right\}$. 

于是我们有

$$
\begin{cases}
\ket{\psi_i}=\sum_kA_{ki}\ket{k},& \braket ij=\delta_{ij}\\
\ket{\widetilde \psi_i}=\sum_kA_{ki}\ket{\widetilde k},& \braket{\widetilde i}{\widetilde j}=\delta_{ij}
\end{cases}
$$

由题 2 知, 对于正交归一化态, 我们可以构造酉变换 $U=\sum_i\ketbra{\widetilde i}i$ 使得 $U\ket i=\ket{\widetilde i}$.

此时有
$$
U\ket{\psi_i}=U\sum_kA_{ki}\ket{k}=\sum_kA_{ki}U\ket{k}=\sum_kA_{ki}\ket{\widetilde k}=\ket{\widetilde \psi_i}
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



### 5. 对三粒子系统纯态 $\ket{\phi}_{ABC}$，在空间 $\H_A\otimes\H_B\otimes\H_C$ 中是否存在 $\H_A$, $\H_B$, $\H_C$ 中的正交基 $\left\{\ket{i_A}\right\}$, $\left\{\ket{i_B}\right\}$, $\left\{\ket{i_C}\right\}$, 使得 $\ket{\phi}_{ABC}=\sum_i{\sqrt{p_i}\ket{i_A}\otimes\ket{i_B}\otimes\ket{i_C}}$ 一定成立? 给出理由.

不一定成立. 下用反证法证之.

**证明**:

假设原命题成立, 即 $\ket{\phi}_{ABC}=\sum_i{\sqrt{p_i}\ket{i_A}\otimes\ket{i_B}\otimes\ket{i_C}}$.

则有密度矩阵形式
$$
\rho_{ABC}=\ket\phi_{ABC}\bra\phi=\sum_{ij}{
	\sqrt{p_ip_j}\cdot\ket i_A\bra j\otimes\ket i_B\bra j\otimes\ket i_C\bra j
}
$$
对 $\H_B$, $\H_C$ 求部分迹得
$$
\begin{equation}
\begin{aligned}
\rho_A
&=\Tr\left(\rho_{ABC}\right)\\
&=\sum_{kl}{
	\sideset{_C}{_C}{\bra l\sideset{_B}{_B}{\bra k\rho_{ABC}\ket k}\ket l}
}\\

&=\sum_{ijkl}\sqrt{p_ip_j}\cdot\ket i_A\bra j\cdot\delta_{ki}\delta_{jk}\delta_{li}\delta_{jl}\\
&=\sum_i{p_i\ket i_A\bra i}
\end{aligned}
\end{equation}
$$
同理可得
$$
\begin{align}
\rho_B&=\sum_i{p_i\ket i_B\bra i}\\
\rho_C&=\sum_i{p_i\ket i_C\bra i}\\
\end{align}
$$
从而 $\rho_A$, $\rho_B$, $\rho_C$ 具有相同的本征值.

然而, 事实上 $\rho_A$, $\rho_B$, $\rho_C$ 可以有不同的本征值, 下面给出反例

考虑两能级系统, 令 $\ket\phi_{ABC}=\frac1{\sqrt2}\left(\ket{000}_{ABC}+\ket{010}_{ABC}\right)$, 则有
$$
\begin{equation*}
\rho_{AB}
=\sideset{_C}{_C}{\bra0\rho_{ABC}\ket0}
+\sideset{_C}{_C}{\bra1\rho_{ABC}\ket1}
=\frac12\left(
	\ket{00}_{AB}\bra{00}+\ket{01}_{AB}\bra{01}
\right)\\
\rho_{A}
=\sideset{_B}{_B}{\bra0\rho_{AB}\ket0}
+\sideset{_B}{_B}{\bra1\rho_{AB}\ket1}
=\ket{0}_{A}\bra{0}\\
\rho_{B}
=\sideset{_A}{_A}{\bra0\rho_{AB}\ket0}
+\sideset{_A}{_A}{\bra1\rho_{AB}\ket1}
=\frac12\left(
	\ket{0}_{B}\bra{0}+\ket{1}_{B}\bra{1}
\right)\\
\end{equation*}
$$
此时 $\rho_A$, $\rho_B$ 有着不同的本征值.

故假设不成立, 得证.



### 6. 设 $\ket\psi$ 为量子比特态，在 *Bloch* 球面上均匀随机分布. 

#### (i) 随机地猜想一个态 $\ket\phi$，求猜测态相对于 $\ket\psi$ 的平均保真度 $\bar F=<\abs{\braket\phi\psi}^2>$.

不妨设 $\psi=\ket0$, 而 $\ket\phi$ 为 *Bloch* 球面上的任意态
$$
\ket\phi=\ket{\phi(\theta,\varphi)}=\cos\frac\theta2\ket0+e^{\mathrm i\varphi}\sin\frac\theta2\ket1
$$
则平均保真度
$$
\begin{align*}
\bar F&=<\abs{\braket\phi\psi}^2>=<\cos^2\frac\theta2>\\
&=\frac1{4\pi}\int_0^{2\pi}\mathrm{d}\varphi\int_0^\pi{
	\cos^2\frac\theta2\sin\theta\mathrm{d}\theta
}\\
&=-\frac12\int_0^\pi{
	\frac{1+\cos\theta}2\mathrm d\cos\theta
}\\
&=-\frac12\int_0^\pi{
	\mathrm d\left(\frac{\cos\theta}2+\frac{\cos^2\theta}4\right)
}\\
&=\frac12
\end{align*}
$$


#### (ii) 对此量子态做正交测量 $\left\{P_\uparrow,P_\downarrow\right\}$, 其中 $P_\uparrow+P_\downarrow=I$. 测量后系统被制备到: $\rho$, 求 $\rho$ 与原来的态 $\ket\psi$ 的平均保真度 $\bar F=<\bra\psi\rho\ket\psi>$.

以 $\ket\uparrow$, $\ket\downarrow$ 为基, 将 $\ket\psi$ 表示为
$$
\ket\psi=\cos\frac\theta2\ket\uparrow+e^{\mathrm i\varphi}\sin\frac\theta2\ket\downarrow
$$
测量后的 $\rho$ 表示成混合态系综的形式
$$
\rho=\bra\psi P_\uparrow\ket\psi\cdot P_\uparrow+\bra\psi P_\downarrow\ket\psi\cdot P_\downarrow=\cos^2\frac\theta2P_\uparrow+\sin^2\frac\theta2P_\downarrow
$$
于是
$$
\bra\psi\rho\ket\psi=\cos^4\frac\theta2+\sin^4\frac\theta2
$$
从而
$$
\begin{align*}
\bar F&=<\cos^4\frac\theta2+\sin^4\frac\theta2>\\
&=\frac1{4\pi}\int_0^{2\pi}\mathrm{d}\varphi\int_0^\pi{
	\left(\cos^4\frac\theta2+\sin^4\frac\theta2\right)\sin\theta\mathrm{d}\theta
}\\
&=-\frac12\int_0^\pi{
	\left[
		\left(\frac{1+\cos\theta}2\right)^2 + \left(\frac{1-\cos\theta}2\right)^2
	\right]
	\mathrm d\cos\theta
}\\

&=-\frac14\int_0^\pi{
	\left(
		1+\cos^2\theta
	\right)
	\mathrm d\cos\theta
}\\

&=-\frac14\int_0^\pi{
	\mathrm d\left(
		\cos\theta+\frac{\cos^3\theta}3
	\right)
}\\
&=\frac23
\end{align*}
$$


### 7. $\ket{\psi_1}=\ket0$, $\ket{\psi_2}=-\frac12\ket0+\frac{\sqrt3}2\ket1$, $\ket{\psi_3}=-\frac12\ket0-\frac{\sqrt3}2\ket1$. 现令 $F_a=\frac23\ketbra{\psi_a}{\psi_a}$，则 $\left\{F_a\right\}_{a=1,2,3}$ 构成二维空间中的 *POVM*. 现引入一个辅助的 *qubit*, 试在扩展空间中实施一个正交测量, 从而实现此 *POVM*.

已知 $F_a=\frac23\ketbra{\psi_a}{\psi_a}=\ketbra{\widetilde\psi_a}{\widetilde\psi_a}$, 故 $\ket{\widetilde\psi_a}=\sqrt{\frac23}\ket{\psi_a}$.

于是有
$$
\pmatrix{\ket{\widetilde\psi_1}&\ket{\widetilde\psi_2}&\ket{\widetilde\psi_3}}
=\pmatrix{
\sqrt\frac23	&	-\sqrt\frac16	&	-\sqrt\frac16\\
0				&	\sqrt\frac12	&	-\sqrt\frac12
}
$$
共三个测量算符, 故做直和扩展到三维空间, $\ket{u_a}=\ket{\widetilde\psi_a}+\ket{\widetilde\psi_a^\perp}$. 

现在只需找到一个与 $\pmatrix{\ket{\widetilde\psi_1}&\ket{\widetilde\psi_2}&\ket{\widetilde\psi_3}}$ 中的行向量均正交的向量, 易得 $\sqrt\frac13(1,1,1)$ 满足条件. 于是我们得到
$$
\pmatrix{\ket{u_1}&\ket{u_2}&\ket{u_3}}
=\pmatrix{
\sqrt\frac23	&	-\sqrt\frac16	&	-\sqrt\frac16\\
0				&	\sqrt\frac12	&	-\sqrt\frac12\\
\sqrt\frac13	&	\sqrt\frac13	&	\sqrt\frac13
}
$$
现在再引入一个辅助 *qubit* 做直积扩展,  $\ket{\Phi_a}=\ket{0}\ket{\widetilde \psi_a}+\ket{1}\ket{\widetilde\psi_{1a}^\perp}$, 此时为 4 维空间, 需要引入额外的正交向量.

于是我们有
$$
\pmatrix{\ket{\Phi_1}&\ket{\Phi_2}&\ket{\Phi_3}&\ket{\Phi_4}}
=\pmatrix{
\sqrt\frac23	&	-\sqrt\frac16	&	-\sqrt\frac16	&	0\\
0				&	\sqrt\frac12	&	-\sqrt\frac12	&	0\\
\sqrt\frac13	&	\sqrt\frac13	&	\sqrt\frac13	&	0\\
0				&	0				&	0				&	1\\
}
$$
令 $E_a=\ketbra{\Phi_a}{\Phi_a}$, 则 $\left\{E_a\right\}_{a=1,2,3,4}$ 在题设扩展空间中实现了此 POVM.



### 8\*. 证明超算符仅在幺正条件下才是可逆的.

**证明**:

考虑 $\H_A$ 空间的超算符, 用算符和表示为
$$
$(\rho_A)=\sum_\mu M_\mu\rho_A M_\mu^\dagger
$$
算符的个数记为 $N$.

给定算符和表示后, 可以创造一个相应的幺正表示
$$
U_{AB}:\ket\varphi_A\otimes\ket0_B\rightarrow\sum_\mu{M_\mu\ket\varphi_A\otimes\ket\mu_B}
$$
其中 $\ket \mu_B$ 为 $\mathcal H_B$ 中的一组正交基. 由混态的统计解释，这种表示对一般的混合态也成立.

对于 $\H_A\otimes\H_B$ 空间中的逆变换 $U_{AB}^{-1}=U_{AB}^\dagger$, 

记 $U_{AB}^{-1}$ 在子系统 $\H_A$ 中的超算符为 $\$'$, 相应的算符为 $M'_\mu$, 算符个数记为 $N'$.

于是我们有
$$
\begin{equation}
\begin{aligned}
$'$(\rho_A)
&=\sum_\nu{
	M_\nu'^\dagger
	\left(\sum_\mu
		M_\mu\rho_AM_\mu^\dagger
	\right)
	M'_\nu
}\\

&=\sum_{\nu\mu}{
M_\nu'^\dagger M_\mu\rho_AM_\mu^\dagger M'_\nu
}\\

&=\sum_{\nu\mu}{
(M_\nu'^\dagger M_\mu)\rho_A(M_\nu'^\dagger M_\mu)^\dagger
}\\

\end{aligned}
\end{equation}
$$
$\$'\$$ 对应的算符个数为 $N'N$.

令 $n=N(\nu-1)+\mu$, $K_n=M_\nu'^\dagger M_\mu$, 则
$$
$'$(\rho_A)=\sum_n{
	K_n\rho_AK_n^\dagger
}
$$
要令超算符可逆, 亦即 $\$'\$(\rho_A)=\rho_A$, 则必须令 $N'N=1$. 此时 $N'=N=1$, 有
$$
$(\rho_A)=M_1\rho_AM_1^\dagger,\qquad M_1^\dagger M_1=I
$$
即超算符是幺正的. 

因此超算符可逆时必须是幺正的. 证毕.



