# Scores 

## Scores

- A (linear) "score" is an artificially created feature that is a linear combination of existing features.

$$
S_j = \sum a_{i} x_{ji}
$$

- A score is defined by $k$ weights 
$$
\left[ \begin{array}{c} a_1 \\ a_2 \\ \vdots \\ a_k\end{array}\right]
$$

and the values of a score on the samples is computed by

$$
\left[\begin{array}{c} S_{1} \\ S_{2}\\ \vdots \\ S_{n}\end{array}\right] = X_{0}\left[ \begin{array}{c} a_1 \\ a_2 \\ \vdots \\ a_k\end{array}\right]
$$

\newpage
## Mean of scores

A linear combination of features with mean zero has mean zero.


\newpage
## Variance and Covariance of scores

If $S$ is a score corresponding to a weight vector $a$, then

$$
\sigma_{S}^2 = a^{\intercal}D_{0}a.
$$

If $S$ and $T$ are two scores corresponding to weights $a$ and $b$, then
the covariance of $S$ and $T$ is given by

$$
\sigma_{ST} = b^{\intercal}D_{0}a.
$$







