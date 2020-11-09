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
# 第三次作业

## 补充作业2

### 1. 判定下列组合中, 纯态是否是相应混态的纯化态. 如果是, 求出其对应纯态的 Schmidt 分解形式; 如果不是, 是否存在单方的局域幺正操作, 将其变换成到相应混合量子态的纯化态?

#### (a)

$$
\begin{equation*}
\rho=\frac34\ketbra00+\frac14\ketbra11\\

\ket\psi=\frac{\sqrt3+1}4\left(\ket{00}+\ket{11}\right)+\frac{\sqrt3-1}4\left(\ket{01}+\ket{10}\right)
\end{equation*}
$$

**解**: 不妨设 $\ket\psi$ 所在的 Hilbert 空间为 $\H_A\otimes\H_B$, 则 $A$ 空间的约化密度矩阵为
$$
\mleq{
    \rho_A&=\Tr_B\left(\ketbra{\psi_{AB}}{\psi_{AB}}\right)\\
    &=\sideset{_B}{_B}{\bra0\cdot\ketbra{\psi_{AB}}{\psi_{AB}}\cdot\ket0}
    	+\sideset{_B}{_B}{\bra1\cdot\ketbra{\psi_{AB}}{\psi_{AB}}\cdot\ket1}\\
    &=\frac12(\ket0_A\bra0+\ket1_A\bra1)+\frac14(\ket0_A\bra1+\ket1_A\bra0)\\
    &=\frac34\ket+_A\bra++\frac14\ket-_A\bra-
}
$$
其中$\ket\pm=\frac1{\sqrt2}(\ket0\pm\ket1)$.

显然 $\rho_A\ne\rho$, 故 $\ket\psi$ 不是相应混态 $\rho$ 的纯化态.

由 GHJW 定理易知, $B$ 空间的任意酉变换不会改变 $\rho_A$, 所以我们只能尝试在 $A$ 空间做酉变换.

本题我们能直接看到 $\rho_A$ 和 $\rho$ 在不同基矢下有着相同的矩阵元, 显然两者可以通过 Hadamard 变换 $H=\frac1{\sqrt2}\pmatrix{1&1\\1&-1}$ 相联系. 

于是我们只需要对 $\ket\psi$ 做单方的局域幺正操作 $H_A\otimes I_B$ 即可将其变换成 $\rho$ 的纯化态.



#### (b) 

$$
\begin{equation*}
\rho=\frac34\ketbra{\Phi^+}{\Phi^+}+\frac1{16}I\otimes I\\

\ket\psi=\frac{\sqrt7}4\left(\ket{000}+\ket{010}\right)+\frac14\left(\ket{101}-\ket{111}\right)
\end{equation*}
$$

**解**: 不妨设 $\ket\psi$ 所在的 Hilbert 空间为 $\H_A\otimes\H_B\otimes\H_C$, 

对 $A$ 求部分迹有
$$
\begin{equation}
\begin{aligned}
\rho_{BC}&=\Tr_A(\ketbra{\psi_{ABC}}{\psi_{ABC}})\\
&=\frac{\sqrt7}4\left(\ket{00}+\ket{10}\right)\cdot\frac{\sqrt7}4\left(\bra{00}+\bra{10}\right)\\
&\quad+\frac14\left(\ket{01}-\ket{11}\right)\cdot\frac14\left(\bra{01}-\bra{11}\right)\\
&=\frac78\ketbra\alpha\alpha+\frac18\ketbra\beta\beta
\end{aligned}
\end{equation}
$$
对 $B$ 求部分迹有
$$
\begin{equation}
\begin{aligned}
\rho_{AC}&=\Tr_B(\ketbra{\psi_{ABC}}{\psi_{ABC}})\\
&=\left(\frac{\sqrt7}4\ket{00}+\frac14\ket{11}\right)\cdot\left(\frac{\sqrt7}4\bra{00}+\frac14\bra{11}\right)\\
&\quad+\left(\frac{\sqrt7}4\ket{00}-\frac14\ket{11}\right)\cdot\left(\frac{\sqrt7}4\bra{00}-\frac14\bra{11}\right)\\
&=\frac78\ketbra{00}{00}+\frac18\ketbra{11}{11}
\end{aligned}
\end{equation}
$$
对 $C$ 求部分迹有
$$
\begin{equation}
\begin{aligned}
\rho_{BC}&=\Tr_A(\ketbra{\psi_{ABC}}{\psi_{ABC}})\\
&=\frac{\sqrt7}4\left(\ket{00}+\ket{01}\right)\cdot\frac{\sqrt7}4\left(\bra{00}+\bra{01}\right)\\
&\quad+\frac14\left(\ket{10}-\ket{11}\right)\cdot\frac14\left(\bra{10}-\bra{11}\right)\\
&=\frac78\ketbra{\alpha'}{\alpha'}+\frac18\ketbra{\beta'}{\beta'}
\end{aligned}
\end{equation}
$$
易知三者有相同的本征值 $\frac78,\frac18,0,0$.

而对于混态 $\rho$ 有
$$
\rho=\frac34\ketbra{\Phi^+}{\Phi^+}+\frac1{16}I\otimes I=\pmatrix{
	\frac7{16}	&				&				& \frac38	\\
				& \frac1{16}	& 				&			\\
				&				& \frac1{16}	& 			\\
	\frac38		&				&				& \frac7{16}\\
}
$$
令 $\det(\lambda I-\rho)=0$, 解得本征值为 $\frac{13}{16},\frac1{16},\frac1{16},\frac1{16}$.

本征值不同, 显然 $\ket\psi$ 并非 $\rho$ 的纯化态. 由于幺正变换不改变本征值, 因此也不存在幺正变换使之变为 $\rho$ 的纯化态.



### 2. 现有一个主系统 $A$ 和一个辅助系统 $B$ 组成的联合量子比特系统$\H_A\otimes\H_B$, 分别作用下面的联合么正操作: $U_1=\ketbra00\otimes I+\ketbra11\otimes X$, $U_2=\frac1{\sqrt2}\left(X\otimes I+Y\otimes X\right)$, 其中 $X$, $Y$, $Z$ 为泡利矩阵，假定辅助系统的初始态为 $\ket0$.
#### (a）试分别写出 $U_1$ 和 $U_2$ 在主系统中的算符和表示. 

由于辅助系统初态为 $\ket0$, 故有
$$
\begin{equation}
\begin{aligned}
\rho_A'=\$(\rho_A)&=\Tr_B(U_{AB}(\rho_A\otimes\ket0_B\bra0)U_{AB}^\dagger)\\
&=\sum_\mu{
	\sideset{_B}{_B}{\bra\mu U_{AB}\ket0}\rho_A\sideset{_B}{_B}{\bra0 U_{AB}^\dagger\ket\mu}
}\\
&=\sum_\mu{
	M_\mu\rho_AM_\mu^\dagger
}
\end{aligned}
\end{equation}
$$

于是 $M_\mu=\sideset{_B}{_B}{\bra\mu U_{AB}\ket0}$.

从而对于 $U_1$, 有
$$
\begin{align}
M_0^{(1)}&=\sideset{_B}{_B}{\bra0 U_1\ket0}=\ketbra00\\
M_1^{(1)}&=\sideset{_B}{_B}{\bra1 U_1\ket0}=\ketbra11
\end{align}
$$
对于 $U_2$, 有
$$
\begin{align}
M_0^{(2)}&=\sideset{_B}{_B}{\bra0 U_2\ket0}=\frac1{\sqrt2}X\\
M_1^{(2)}&=\sideset{_B}{_B}{\bra1 U_2\ket0}=\frac1{\sqrt2}Y
\end{align}
$$


#### (b) 如果考虑联合作用 $U = U_1U_2$，取同样的辅助系统的初始态为 $\ket0$，写出其算符和形式；并验证该算符和是否对应 $U_1$ 和 $U_2$ 各自对应超算符 $\xi_1$ 和 $\xi_2$ 的联合 $\xi = \xi_1\xi_2$.

对 $U=U_1U_2=\frac1{\sqrt2}(\ketbra01\otimes I+\ketbra10\otimes X+i\ketbra01\otimes X-i\ketbra10\otimes I)$ , 有
$$
\begin{align}
M_0^{(1,2)}&=\sideset{_B}{_B}{\bra0 U_1U_2\ket0}=\frac1{\sqrt2}\left(\ketbra01-i\ketbra10\right)\\
M_1^{(1,2)}&=\sideset{_B}{_B}{\bra1 U_1U_2\ket0}=\frac1{\sqrt2}\left(\ketbra10+i\ketbra01\right)
\end{align}
$$
而对于 $\xi=\xi_1\xi_2$, 有
$$
\xi(\rho_A)=\xi_1\left(\xi_2(\rho_A)\right)=\sum_\nu\sum_\mu{
	M_\nu^{(1)}M_\mu^{(2)}\rho_A M_\mu^{(2)\dagger}M_\nu^{(1)\dagger}=\sum_{\nu\mu}M_{\nu\mu}\rho_AM_{\nu\mu}^\dagger
}
$$
从而
$$
\begin{align}
M_{00}=M_0^{(1)}M_0^{(2)}=\frac1{\sqrt2}\ketbra01\\
M_{01}=M_0^{(1)}M_1^{(2)}=\frac i{\sqrt2}\ketbra01\\
M_{10}=M_1^{(1)}M_0^{(2)}=\frac1{\sqrt2}\ketbra10\\
M_{11}=M_1^{(1)}M_1^{(2)}=\frac {-i}{\sqrt2}\ketbra10
\end{align}
$$
显然两者并不对应.



### 3.假定有一个超算符演化满足 $\xi(\rho)=\frac pdI+(1-p)\rho$, 其中 $p$ 为小于等于 1 的实数, $d$表示系统的维数,试在 $d=2$ 时，构造出该演化的算符和形式. 如果 $d=3$,该如何构造？

先讨论 $d=2$ 的情形, 此时可以将密度矩阵表示为
$$
\rho=\frac{I+\boldsymbol\sigma\cdot \boldsymbol r}2
$$
我们先给出如下 Pauli 矩阵的性质 (其中 $X$, $Y$, $Z$, $\sigma_i$ 均表示 Pauli矩阵)

| $\sigma_i$ | $X\sigma_i X^\dagger$ | $Y\sigma_i Y^\dagger$ | $Z\sigma_iZ^\dagger$ |
| ---------- | --------------------- | --------------------- | -------------------- |
| $\sigma_x$ | $\sigma_x$            | -$\sigma_x$           | -$\sigma_x$          |
| $\sigma_y$ | -$\sigma_y$           | $\sigma_y$            | -$\sigma_y$          |
| $\sigma_z$ | -$\sigma_z$           | -$\sigma_z$           | $\sigma_z$           |

于是我们发现
$$
X\rho X^\dagger+Y\rho Y^\dagger+Z\rho Z^\dagger=\frac{3I-\boldsymbol\sigma\cdot \boldsymbol r}2=2I-\rho
$$
现在我们将超算符 $\xi(\rho)$ 改写为
$$
\xi(\rho)=\frac p4(2I-\rho)+(1-\frac{3p}4)\rho
$$
于是我们可以构造出以下 Kraus 算子
$$
M_0=\sqrt{1-\frac {3p}4}\cdot I,\quad M_1=\sqrt\frac p4X, \quad M_2=\sqrt\frac p4Y, \quad M_3=\sqrt\frac p4Z,
$$
$d=3$ 时不会算.



### 8*：证明超算符仅在幺正条件下才是可逆的. (选做思考题) 

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



### 9. 证明 $\ket{\Psi^-}=\frac1{\sqrt2}\left(\ket0\ket1-\ket1\ket0\right)$ 在 $U(\vartheta,\hat{\boldsymbol n})\otimes U(\vartheta,\hat{\boldsymbol n})$ 下是不变的.

**证**: $U(\vartheta,\hat{\boldsymbol n})$可以写为
$$
U(\vartheta,\boldsymbol n)=\exp(i\frac\vartheta2\boldsymbol\sigma\cdot \hat{\boldsymbol n})=I\cos\frac\vartheta2-i\boldsymbol\sigma\cdot \hat{\boldsymbol n}\sin\frac\vartheta2
$$
其中 $\hat{\boldsymbol n}=(n_1,n_2,n_3)^T$.

于是我们有
$$
\begin{align}
U(\vartheta,\hat{\boldsymbol n})\ket0&=(\cos\frac\vartheta2-in_3\sin\frac\vartheta2)\ket0-(in_1-n_2)\sin\frac\vartheta2\ket1\\
U(\vartheta,\hat{\boldsymbol n})\ket1&=(\cos\frac\vartheta2+in_3\sin\frac\vartheta2)\ket1-(in_1+n_2)\sin\frac\vartheta2\ket0
\end{align}
$$
从而
$$
\mleq{
&U(\vartheta,\hat{\boldsymbol n})\otimes U(\vartheta,\hat{\boldsymbol n})\ket{\Psi^-}\\
=&\frac1{\sqrt2}\left[U(\vartheta,\hat{\boldsymbol n})\ket0\otimes U(\vartheta,\hat{\boldsymbol n})\ket1-U(\vartheta,\hat{\boldsymbol n})\ket1\otimes U(\vartheta,\hat{\boldsymbol n})\ket0\right]\\
=&\frac1{\sqrt2}\left[(\cos\frac\vartheta2-in_3\sin\frac\vartheta2)(\cos\frac\vartheta2+in_3\sin\frac\vartheta2)-(in_1+n_2)(in_1-n_2)\sin^2\frac\vartheta2\right]\ket0\ket1\\
&+\frac1{\sqrt2}\left[(in_1-n_2)(in_1+n_2)\sin^2\frac\vartheta2-(\cos\frac\vartheta2+in_3\sin\frac\vartheta2)(\cos\frac\vartheta2-in_3\sin\frac\vartheta2)\right]\ket1\ket0\\
=&\frac1{\sqrt2}\left[\cos^2\frac\vartheta2+(n_1^2+n_2^2+n_3^2)\sin^2\frac\vartheta2\right]\ket0\ket1\\
&-\frac1{\sqrt2}\left[\cos^2\frac\vartheta2+(n_1^2+n_2^2+n_3^2)\sin^2\frac\vartheta2\right]\ket1\ket0\\
=&\frac1{\sqrt2}\left(\ket0\ket1-\ket1\ket0\right)
}
$$

证毕.




## 补充习题3

### 1. 试证明相对熵纠缠度量在纯态情况下和 Von Neumann 熵是等价的. 即求任意给定纯态 $\ket{\psi_{AB}}$ 和任意混合态 $\sum_i{p_i\rho_i\otimes\sigma_i}$ 中的最小相对熵 $S(\ketbra{\psi_{AB}}{\psi_{AB}}||\sum_i{p_i\rho_i\otimes\sigma_i})$.



### 2. 计算混合量子态 $\rho=p\ketbra{\Phi^+}{\Phi^+}+\frac{1-p}4I\otimes I$ 的纠缠 concurrence，其中 $0\le p\le1$，$\ket{\Phi^+}$ 是 Bell 态.

已知
$$
\mleq{
\rho&=p\ketbra{\Phi^+}{\Phi^+}+\frac{1-p}4\sum_{\ket\alpha\in \mathrm{Bell\,State}}\ketbra\alpha\alpha\\
&=\frac{1+3p}4\ketbra{\Phi^+}{\Phi^+}+\frac{1-p}4\left(\ketbra{\Phi^-}{\Phi^-}+\ketbra{\Psi^+}{\Psi^+}+\ketbra{\Psi^-}{\Psi^-}\right)
}
$$

由于
$$
\cases{
	\sigma_y\otimes\sigma_y\ket{\Phi^+}=-\ket{\Phi^+}\\
	\sigma_y\otimes\sigma_y\ket{\Phi^-}=+\ket{\Phi^-}\\
	\sigma_y\otimes\sigma_y\ket{\Psi^+}=+\ket{\Psi^+}\\
	\sigma_y\otimes\sigma_y\ket{\Psi^-}=-\ket{\Psi^-}\\
}
$$
故
$$
\tilde\rho=(\sigma_y\otimes\sigma_y)\rho^*(\sigma_y\otimes\sigma_y)=\rho
$$

从而
$$
\mleq{
R&=\sqrt{\sqrt\rho\tilde\rho\sqrt\rho}\\
&=\sqrt{U\sqrt\Lambda U^\dagger \cdot U\Lambda U^\dagger \cdot U\sqrt\Lambda U^\dagger}\\
&=\sqrt{U\Lambda^2U^\dagger}\\
&=U\Lambda U^\dagger\\
&=\rho
}
$$
由式 (31) 易知 $\rho$ 的本征值为 $\frac{1+3p}4$, $\frac{1-p}4$, $\frac{1-p}4$, $\frac{1-p}4$.

故纠缠 Concurrence
$$
C(\rho)=\max\left\{\frac{1+3p}4-3\cdot\frac{1-p}4,\quad0\right\}=\max\left\{\frac{3p-1}2,\quad0\right\}
$$


### 3. 相对熵的单调性(Lindblad-Uhlmann定理)是说，复合系统中两混合态的相对熵大于其约化子系统中量子态的相对熵，数学表示为 $S(\rho_A|\sigma_A)\le S(\rho_{AB}|\sigma_{AB})$. 试利用该定理证明下面结论：

#### (a) 考察三体态 $\rho_{ABC}$ 和 $\rho_A\otimes\rho_{BC}$ 之间的相对熵, 并证明 Von Neumann 熵的强次加定理.



#### (b) 利用超算符对应于扩张空间的某个酉变换, 证明相对熵在超算符演化下不增加，亦即 $S(\$\rho|\$\sigma)\le S(\rho|\sigma)$.



#### (c) 利用b中的结果，证明超算符演化下，混合态系综 $\varepsilon=\left\{p_x,\rho_x\right\}$ 的 Holevo 信息不会增加，亦即 $\chi\left(\$(\varepsilon)\right)\le\xi(\varepsilon)$，其中 $\xi(\varepsilon)=S(\sum_x{p_x\rho_X})-\sum_x{p_xS(\rho_x)}$.



### 10. 证明 $S(\rho_A)+S(\rho_B)\le S(\rho_{AC})+S(\rho_{BC})$.



### 11. 考虑 2－qubit 系统 $\rho_{AB}=\frac18I\otimes I+\frac12\ketbra{\Psi^-}{\Psi^-}$, 分别沿 $\hat m$, $\hat n$ 方向测 $A$, $B$ 粒子的自旋. 其中 $\hat m\cdot\hat n=\cos\vartheta$, 则测量结果均为向上的联合概率是多少? 由 Peres-Horodeski 判据，确定 $\rho_{AB}$ 是否为可分量子态.