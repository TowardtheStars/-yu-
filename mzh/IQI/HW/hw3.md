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
# 第三次作业

## 补充作业2

### 1. 判定下列组合中, 纯态是否是相应混态的纯化态. 如果是, 求出其对应纯态的Schmidt分解形式; 如果不是, 是否存在单方的局域幺正操作, 将其变换成到相应混合量子态的纯化态?

#### (a)

$$
\begin{equation*}
\rho=\frac34\ketbra00+\frac14\ketbra11\\

\ket\psi=\frac{\sqrt3+1}4\left(\ket{00}+\ket{11}\right)+\frac{\sqrt3-1}4\left(\ket{01}+\ket{10}\right)
\end{equation*}
$$

**解**



#### (b) 

$$
\begin{equation*}
\rho=\frac34\ketbra{\Phi^+}{\Phi^+}+\frac1{16}I\otimes I\\

\ket\psi=\frac{\sqrt7}4\left(\ket{000}+\ket{010}\right)+\frac14\left(\ket{101}-\ket{111}\right)
\end{equation*}
$$

**解**



### 2. 现有一个主系统 $A$ 和一个辅助系统 $B$ 组成的联合量子比特系统$\H_A\otimes\H_B$, 分别作用下面的联合么正操作: $U_1=\ketbra00\otimes I+\ketbra11\otimes X$, $U_2=\frac1{\sqrt2}\left(X\otimes I+Y\otimes X\right)$, 其中 $X$, $Y$, $Z$ 为泡利矩阵，假定辅助系统的初始态为 $\ket0$.
#### (a）试分别写出 $U_1$ 和 $U_2$ 在主系统中的算符和表示. 
#### (b) 如果考虑联合作用 $U = U_1U_2$，取同样的辅助系统的初始态为 $\ket0$，写出其算符和形式；并验证该算符和是否对应 $U_1$ 和 $U_2$ 各自对应超算符 $\xi_1$ 和 $\xi_2$ 的联合 $\xi = \xi_1\xi_2$.



### 3.假定有一个超算符演化满足 $\xi(\rho)=\frac pdI+(1-p)\rho$, 其中 $p$ 为小于等于 1 的实数, $d$表示系统的维数,试在 $d=2$ 时，构造出该演化的算符和形式. 如果 $d=3$,该如何构造？



### 8*：证明超算符仅在幺正条件下才是可逆的。(选做思考题) 

上次做过了



### 9. 证明 $\ket{\Psi^-}=\frac1{\sqrt2}\left(\ketbra01-\ketbra10\right)$ 在 $U(\vartheta,\boldsymbol n)\otimes U(\vartheta,\boldsymbol n)$ 下是不变的.



## 补充习题3

### 1. 试证明相对熵纠缠度量在纯态情况下和 Von Neumann 熵是等价的. 即求任意给定纯态 $\ket{\psi_{AB}}$ 和任意混合态 $\sum_i{p_i\rho_i\otimes\sigma_i}$ 中的最小相对熵 $S(\ketbra{\psi_{AB}}{\psi_{AB}}||\sum_i{p_i\rho_i\otimes\sigma_i})$.



### 2. 计算混合量子态 $\rho=p\ketbra{\Phi^+}{\Phi^+}+\frac{1-p}4I\otimes I$ 的纠缠concurrence，其中 $0\le p\le1$，$\ket{\Phi^+}$ 是 Bell 态.


### 3. 相对熵的单调性(Lindblad-Uhlmann定理)是说，复合系统中两混合态的相对熵大于其约化子系统中量子态的相对熵，数学表示为 $S(\rho_A|\sigma_A)\le S(\rho_{AB}|\sigma_{AB})$. 试利用该定理证明下面结论：

#### (a) 考察三体态 $\rho_{ABC}$ 和 $\rho_A\otimes\rho_{BC}$ 之间的相对熵, 并证明 Von Neumann 熵的强次加定理.



#### (b) 利用超算符对应于扩张空间的某个酉变换, 证明相对熵在超算符演化下不增加，亦即 $S(\$\rho|\$\sigma)\le S(\rho|\sigma)$.



#### (c) 利用b中的结果，证明超算符演化下，混合态系综 $\varepsilon=\left\{p_x,\rho_x\right\}$ 的 Holevo 信息不会增加，亦即 $\chi\left(\$(\varepsilon)\right)\le\xi(\varepsilon)$，其中 $\xi(\varepsilon)=S(\sum_x{p_x\rho_X})-\sum_x{p_xS(\rho_x)}$.



### 10. 证明 $S(\rho_A)+S(\rho_B)\le S(\rho_{AC})+S(\rho_{BC})$.



### 11. 考虑 2－qubit 系统 $\rho_{AB}=\frac18I\otimes I+\frac12\ketbra{\Psi^-}{\Psi^-}$, 分别沿 $\hat m$, $\hat n$ 方向测 $A$, $B$ 粒子的自旋. 其中 $\hat m\cdot\hat n=\cos\vartheta$, 则测量结果均为向上的联合概率是多少? 由 Peres-Horodeski 判据，确定 $\rho_{AB}$ 是否为可分量子态.