$$
\begin{align*}
\newcommand{\i}{\mathrm{i}}
\end{align*}
$$

## 1.29

### (a)

基本对易关系
$$
\left[x_i,p_j\right]=0,\qquad
\left[x_i,p_j\right]=0,\qquad
\left[x_i,p_j\right]=\i\hbar\delta_{ij}.
$$
可得
$$
\begin{align}
\left[x_i,p_j^2\right]&=\left[x_i,p_j\right]\cdot p_j+p_j\cdot\left[x_i,p_j\right]=2\i\hbar p_j\delta_{ij}\\
\left[x_i,p^2\right]&=\sum_j\left[x_i,p_j^2\right]=\sum_j{2\i\hbar p_j\delta_{ij}}=2\i\hbar p_i\\
\left[x_i,p\right]&=\frac{\left[x_i,p^2\right]}{2p}=\i\hbar p^{-1}p_i
\end{align}
$$

下面给出一个引理

**引理**
$$
\left[x_i,p^n\right]=\i\hbar np^{n-2}p_i
$$

下用数学归纳法证之, 由 (3) (4) 知 $n = 1, 2$ 时成立

假设 $n = k$ 时成立, 即 $\left[x_i,p^k\right]=\i\hbar kp^{k-2}p_i$, 则当 $n=k+1$ 时,
$$
\begin{equation}
\begin{aligned}
\left[x_i,p^{k+1}\right]
&=p\cdot\left[x_i,p^k\right]+\left[x_i,p\right]\cdot p^k\\
&=p\cdot\i\hbar kp^{k-2}p_i+\i\hbar p^{-1}p_i\cdot p^k\\
&=\i\hbar(k+1)p^{k-1}p_i
\end{aligned}
\end{equation}
$$
得证.

我们将 $G(\boldsymbol{p})$ 展开为幂级数
$$
G(\boldsymbol p)=\sum_n
{
	\alpha_n  p^n
}
$$
则待证命题等号左边为
$$
\begin{equation}
\begin{aligned}
\left[x_i,G(\boldsymbol p)\right]
&=\sum_n{\alpha_n\left[x_i,p^n\right]}\\
&=\i\hbar \sum_n{\alpha_nnp^{n-2}p_i}
\end{aligned}
\end{equation}
$$
而
$$
\begin{equation}
\begin{aligned}
\pfrac{G(\boldsymbol p)}{p_i}
&=\sum_n{\alpha_n \pfrac{p^n}{p_i}}\\
&=\sum_n{\alpha_nnp^{n-1}\pfrac{p}{p_i}}\\
&=\sum_n{\alpha_nnp^{n-1}\frac{p_i}{p}}\\
&=\sum_n{\alpha_nnp^{n-2}p_i}\\
\end{aligned}
\end{equation}
$$
故
$$
\left[x_i,G(\boldsymbol p)\right]=\i\hbar\pfrac{G(\boldsymbol p)}{p_i}
$$
得证.

同理可得
$$
\begin{align}
\left[p_i,x^n\right]&=-\i\hbar nx^{n-2}x_i\\
\left[p_i,F(\boldsymbol x)\right]&=-\i\hbar\pfrac{F(\boldsymbol x)}{x_i}
\end{align}
$$
证毕.