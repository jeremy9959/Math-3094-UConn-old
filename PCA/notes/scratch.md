

The covariance matrix $D_{0}$ for the data depicted in +@fig:pcasimfig is
$$
D_{0} = \left(\begin{matrix} .5 & -.75 \\ -.75 & 1.5\end{matrix}\right).
$$
From our earlier discussion of correlation, we see that the correlation coefficient
$$
r = \frac{-.75}{(1.5)(.5)}=-1
$$
so the two features are strongly correlated -- something which is visible in the scatter plot,
but not in the two individual histograms.


Now let's look at the variances of linear combinations of the two basic features.  As we've
seen earlier, if $S=aX+bY$ is a linear combination of the two features, then 
$$
\sigma_{S}^2 = \left[\begin{matrix} a & b \end{matrix}\right]\left(\begin{matrix} .5 & -.75 \\ -.75 & 1.5\end{matrix}\right)\left[\begin{matrix} a \\b\end{matrix}\right] = .5a^2-1.5ab+1.5b^2
$$
