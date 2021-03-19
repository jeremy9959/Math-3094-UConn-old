---
documentclass: extarticle
fontsize: 14pt
---
# Optimal Margin and Closest Points
## Convex Hulls and Margins

Our goal for this section is to reduce the 
optimal margin problem for $A^{\pm}$ to the problem of finding the closest points in the convex hulls
$C(A^{\pm})$.

![Solution](../img/solution.png){height=50%}

\newpage
## Optimal margin vs distance

**Proposition:** The optimal margin between linearly separable sets $A^{\pm}$ is at most
the distance between their convex hulls:
$$
\tau(A^{+},A^{-})\le \min_{{p\in C(A^{+})}\atop{a\in C(A^{-})}} \|p-q\|.
$$

**Proof:**  

- Choose a pair of functions $f^{\pm}(x)=w\cdot x-B^{\pm}$ so that $f^{\pm}(x)=0$ are
supporting hyperplanes for $A^{\pm}$ respectively.

- These are supporting hyperplanes for $C(A^{\pm})$ also.  
\vfill
- If $p$ and $q$ are points in $C(A^{+})$ and $C(A^{-})$ then $w\cdot p-B^{+}\ge 0$ and $w\cdot q-B^{-}\le 0$.
\vfill
- So $w\cdot(p-q)\ge B^{+}-B^{-}>0$.
\vfill
- Therefore 
$$
\|p-q\|\ge \frac{B^{+}-B^{-}}{\|w\|} = \tau_{w}(A^{+},A^{-})
$$
\vfill
- This is true for all $w$. 

\newpage
## More on optimal margin and distance

Two Corollaries:

1.  $A^{\pm}$ are linearly separable if and only if the minimal distance between their convex hulls
is greater than zero.
\vfill
2. If we can find supporting hyperplanes $f^{\pm}=0$ whose margin
**equals** the minimal distance between the convex hulls, then those **must be at** the optimal margin.
\vfill

\newpage


## Convex Hulls and Margins

**Proposition:** Let $A^+$ and $A^-$ be two linearly separable sets.  



1. There are points
$p^*\in C(A^{+})$ and $q^*\in C(A^{-})$ so that 
$$
\|p^{*}-q^{*}\| = D = \min_{{p\in C(A^+)}\atop{q\in C(A^-)}}\|p-q\|.
$$
Further, if $(p_{1}^{*},q_{1}^{*})$ and $(p_{2}^{*},q_{2}^{*})$ are two pairs of points
with $D=\|p_{1}^{*}-q_{1}^{*}\|=\|p_{2}^{*}-q_{2}^{*}\|$ then $p_{1}^{*}-q_{1}^{*}=p_{2}^{*}-q_{2}^{*}$.
![Solution](../img/solution.png){height=50%}

\vfill
\newpage
## Convex Hulls and Margins

2. Let
\begin{enumerate}
\item 	$w=p^{*}-q^{*}$
\item $B^{+}=w\cdot p^{*}$
\item $B^{-}=w\cdot q^{*}$.
\item $f^{\pm}(x)=w\cdot x - B^{\pm}$
\end{enumerate}
Then the hyperplanes $f^{\pm}(x)=0$ are supporting hyperplanes for
$A^{\pm}$ respectively, and the associated margin
$$
\tau_{w}(A^{+},A^{-})=\frac{B^{+}-B^{-}}{\|w\|}=\|p^{*}-q^{*}\|
$$
is optimal.


![Solution](../img/solution.png){height=50%}

\newpage
## Closest points

**Proposition:** Let 
$$
D = \min_{{p\in C(A^{+})}\atop{q\in C(A^{-})}} \|p-q\|.
$$
Then there exist points $p^*\in C(A^{+})$ and $q^{*}\in C(A^{-})$ so that $D=\|p^*-q^*\|$.

\vfill
Suppose further that there  are two pairs of 
points $(p_{1}^{*},q_{1}^{*})$ and $(p_{2}^{*},q_{2}^{*})$ in $C(A^{+})\times C(A^{-})$
with $D=\|p_{1}^{*}-q_{1}^{*}\|=\|p_{2}^{*}-q_{2}^{*}\|$.  Then $p_{1}^{*}-q_{1}^{*}=p_{2}^{*}-q_{2}^{*}$.

\vfill
\newpage

## Proof of the closest point proposition

The function $f(p,q)=\|p-q\|$ on $C(A^{+})\times C(A^{-})$ is a continuous
function on a compact set, so it attains its minimum.  

\vfill

For $0\le s\le 1$, let
$$
p(s) = (1-s)p_{1}^{*}+sp_{2}^{*}
$$
and
$$
q(s) = (1-s)q_{1}^{*}+sq_{2}^{*}.
$$
These points are all in $C(A^{+})$ and $C(A^{-})$ respectively by convexity.  
\vfill
\newpage

Let 
$$
t(s) = \|p(s)-q(s)\|^2.
$$
We must have $t(s)\ge D^2$ for all $s$.  On the other hand
$$
\frac{d}{ds}t(s) = 2(p(s)-q(s))\frac{d}{ds}(p(s)-q(s)) = 2(p(s)-q(s))\cdot ((p_{2}-q_{2})-(p_{1}-q_{1}))
$$
\vfill

Evaluate this at $s=0$ and you get
$$
\frac{d}{ds}t(s) = 2(p_{1}-q_{1})\cdot ((p_{2}-q_{2})-(p_{1}-q_{1}) = 2(v_{1}\cdot v_{2}-\|v_{1}\|^2).
$$
where $v_{1}=p_{1}-q_{1}$ and $v_{2}=p_{2}-q_{2}$. 
\vfill
\newpage

Remember that $\|v_{i}\|^2=D^{2}$ for $i=1,2$ and note that, as a result, $v_{1}\cdot v_{2}\le D^2$.
Therefore
$$
\frac{dt(s)}{ds}|_{s=0} = 2(v_{1}\cdot v_{2}-\|v_{1}\|^2)\le 0
$$

\vfill

If the derivative of $t(s)$ were negative,
$t(s)$ would be decreasing at $s=0$ so there would be a point with $s>0$ where $t(s)<D$.  That can't happen,
since $D$ is the minimal distance, so $v_{1}\cdot v_{2}=D^2$ which means $p^{*}_{1}-q^{*}_{1}=p_{2}^{*}-q_{2}^{*}$.
\vfill

\newpage
## Closest points yield optimal margin

**Proposition:** Let $p$ and $q$ be points in $C(A^{+})$ and $C(A^{-})$ respectively that minimize
the distance between these two sets.   Let $w=p-q$, $B^{+}=w\cdot p$ and $B^{-}=w\cdot q$.

Define hyperplanes
$$
f^{\pm}(x)=w\cdot x - B^{\pm} = 0.
$$

Then $f^{\pm}=0$ are supporting hyperplanes for $C(A^{\pm})$ respectively and the associated margin
$$
\tau_{w}(A^{+},A^{-}) = \frac{B^{+}-B^{-}}{\|w\|}=\|p-q\|
$$
is optimal.
\newpage

## Proof of closest points yield optimal margin

**First Part:** $f^{\pm}(x)=0$ are supporting hyperplanes.

Consider $f^{+}$.  If it is not a supporting hyperplane, there is a point $p'\in C(A^{+})$ so that
$f(p')<0$. 
\vfill
Look at the line segment $t(s)=(1-s)p+sp'$ joining $p$ to $p'$, which lies inside $C(A^{+})$. 
\vfill
Consider the distance $D(s)=\|t(s)-q\|^2$ from points on this line segment to $q$.
\vfill\newpage
We have
\begin{align*}
\frac{dD(s)}{ds}|_{s=0} &= 2(p-q)\cdot (p'-p)=2w\cdot(p'-p) \\
&= 2((f^{+}(p')+B^{+})-(f^{+}(p)+B^{+})) \\
&=  2f^{+}(p') \\
&<0
\end{align*}
\vfill
As in earlier arguments, this is impossible since $p$ is the closest point to $q$ in $C(A^{+})$. 
\vfill
Similarly, $f^{-}$ is a supporting hyperplane.

\vfill
\newpage
## Finishing the proof

**Second Part:**  The margin is $\|p-q\|$. 

Remember that $w=p-q$. Then
$$
\tau_{w} = \frac{B^{+}-B^{-}}{\|w\|} = \frac{w\cdot (p-q)}{\|w\|} = \|p-q\|
$$
This is as large as possible, so it is optimal.
