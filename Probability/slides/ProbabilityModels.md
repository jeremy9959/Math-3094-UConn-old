# Models and Likelihood

## Statistical Models

- Mathematical models

- Statistical models

	- Parameters
	- Likelihood

\newpage
## First example: coin flipping

- Model a coin flipping experiment as a Bernoulli random variable with parameter $p$.

- Flip the coin $100$ times and get $55$ heads and $45$ tails.

$$
L = \binom{100}{55}p^{55}(1-p)^{45}
$$


- **Maximum Likelihood** - forget the constant as it doesn't effect the result.

$$
\frac{dL}{dp} = 55p^{54}(1-p)^{45}-45p^{55}(1-p)^{44} =0
$$

yields 

$$
55(1-p) = 45p
$$

or 

$$
p = 55/100 = .55
$$

\newpage
## Independent normally distributed errors

- Back to our temperature model.  We assume that the errors in our measurements are normally distributed
around zero. There is one parameter: the variance $\sigma^2$
in our density function for a single measurement

$$
p_{\sigma}(x) = \left(\frac{1}{\sigma\sqrt{2\pi}}\right)e^{-x^2/(2\sigma^2)}
$$

-  We make $n$ independent measurements of temperature
$$
x_1,\ldots, x_n
$$
What does this tell us about $\sigma^2$?  The likelihood for independent measurements is the density
$$
L = \left(\frac{1}{\sigma\sqrt{2\pi}}\right)^{n}e^{-\|x\|^2/(2\sigma^2)}
$$

- Maximize the density at this point.  Use the *log-likelihood* as it is easier.

$$
\log P(x) = -n\log\sigma-\frac{\|x\|^2}{2\sigma^2}+C
$$

- Take the derivative and set it equal to zero. 

\vskip 3in


- The *maximum likelihood estimate of the
variance is the mean squared error!*

\newpage
## Linear Regression and likelihood

- Model says that our $N$ data  points $(x_i,y_i)$ arose from a process
$$
y=mx+b+\epsilon
$$
where $\epsilon$ is a normally distributed error term with variance $\sigma^2$.  

- How should we set $m,b,\sigma$ to make the observed data most likely?

- The density function is
$$
P(m,b,\sigma) = \left(\frac{1}{\sigma\sqrt{2\pi}}\right)^{N}e^{-\sum_{i=1}^{N} (y_i-mx_i-b)^2/(2\sigma^2)}
$$

- The *log likelihood* is 
$$
\log P = -N\log\sigma -\frac{1}{2\sigma^2}\sum_{i}(y_{i}-mx_{i}-b)^2
$$

- The derivatives with respect to $m$ and $b$ give the least squares estimates.

\vskip 1in

- The derivative with respect to $\sigma$ gives the best estimate when $\sigma^2$ is the
mean squared error.

\vskip 1in


- **Ordinary Least Squares is the maximum likelihood solution assuming independent normally
distributed errors**
