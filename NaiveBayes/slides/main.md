--- 
pagetitle: Naive Bayes
colorlinks: true 
linkcolor: blue
link-citations: true 
csl: [../../resources/stat.csl]
bibliography: [../../references/references.bib]
reference-section-title: References 
xnos-cleveref: True 
header-includes: |
 <style>
 body {
  max-width: 60em ; 
 }
 </style>
---
\lstset{columns=fullflexible,breaklines=true,basicstyle=\small\ttfamily,backgroundcolor=\color{gray!10}}

# Naive Bayes for Classification

## Sentiment Analysis

- Sentiment analysis is the problem of extracting the author's tone from a piece of text. 

- A simple example is deciding if a product review is positive or negative. Here are some short
reviews of Amazon products, labelled with a 0 if they are negative or a 1 if they are positive.


```
So there is no way for me to plug it in here in the US unless I go by a converter.	0
Good case, Excellent value.	1
Great for the jawbone.	1
Tied to charger for conversations lasting more than 45 minutes.MAJOR PROBLEMS!!	0
The mic is great.	1
```

- We have three files each with 1000 labelled reviews, 500 of which are positive, 500 negative:
  - amazon reviews of products
  - yelp reviews of restaurants
  - imdb reviews of movies

- Our method will be *supervised learning* where we use a set of pre-labelled reviews to develop
an algorithm that we can then apply to new, unlabelled reviews.

- Building a Spam filter is another example of this type of problem.

\newpage
## Bernoulli tests

- Building block: presence or absence of keywords.  Each word is a "test."


|            | + | - | total |
|------------|---|---|-------|
| **great**  |92   | 5  |  97     |
| ~**great** |408   | 495  | 903      |
| total      | 500  | 500  | 1000      |


$$ P (\mathbf{great} | +) =  .184 $$


$$ P(\mathbf{great})  = .097 $$


$$P(+|\mathbf{great}) = .948 $$

$$P(+|\sim\mathbf{great}) = .452$$


|            | + | - | total |
|------------|---|---|-------|
| **waste**  | 0  | 14  | 14     |
| ~**waste** | 500  | 486   | 986      |
| total      | 500  | 500  |  1000     |

\begin{align*}
P(+|\mathbf{waste}) &= 0\\
P(+|\sim\mathbf{waste}) &= .51
\end{align*}

\vfill\eject
## Independence assumption

- We make the (false) assumption that each keyword gives an independent test.

\begin{align*}
P(\mathbf{great},\mathbf{waste}|\pm) &= P(\mathbf{great}|\pm)P(\mathbf{waste}|\pm)\\
P(\mathbf{great},\sim\mathbf{waste}|\pm) &= P(\mathbf{great}|\pm)P(\sim\mathbf{waste}|\pm)\\
 &\vdots \\
\end{align*}

$$
P(+|\mathbf{great},\sim\mathbf{waste}) = \frac{P(\mathbf{great}|+)P(\sim\mathbf{waste}|+)P(+)}{P(\mathbf{great},\sim\mathbf{waste})}
$$

$$
P(-|\mathbf{great},\sim\mathbf{waste}) = \frac{P(\mathbf{great}|-)P(\sim\mathbf{waste}|-)P(-)}{P(\mathbf{great},\sim\mathbf{waste})}
$$

- Decision rule: compare probabilities.  But only the numerator matters -- this is called the "likelihood."

$$
L(+|\mathbf{great},\sim\mathbf{waste}) = (.184)(1)(.5) = .092
$$

$$
L(-|\mathbf{great},\sim\mathbf{waste}) = (.01)(.028)(.5) = .00014
$$

\vfill\eject
## Feature vectors

- Given words $w_1,\ldots, w_k$, with probabilities $P(w_{i}|\pm)$, we imagine independent tests.

- The "naive" probabilities come from the training data:

$$
P(w_{i}|\pm) = \frac{\hbox{\rm number of $\pm$ reviews that include $w_{i}$}}{\hbox{\rm total $\pm$ reviews}}
$$

- All we need to know about a document is whether or not each of the key words appears.

- So a document can be replaced by a vector of $1/0$ (called a "feature vector") where
$f_{i}=1$ if $w_{i}$ appears, and $0$ if it doesn't appear.

\vfill\eject
## Packaging up the data

- Our set of documents can be replaced by an $N\times k$ matrix with entries $0$ and $1$,
with $x_{ij}=1$ if the $j^{th}$ word appears in the $i^{th}$ document.

- Our labels form an $N\times 1$ column vector with entries $0$ (for negative) or $1$ (for positive)
reviews.

- $Y^{\intercal}X$ is  the sum of the rows of $X$ corresponding to positive reviews; it is a $1\times k$
vector whose entries count the number of times $w_{i}$ occurs in a positive document.

- $(1-Y)^{\intercal}X$ is a vector that counts the number of times $w_{i}$ occurs in a negative document.

- $Y^{\intercal}Y=N_{+}$ is the number of positive documents, and $N_{-}=N-N_{+}$.

- The naive probabilities are
$$
P_{+} = \frac{1}{N_{+}}Y^{\intercal}X = \left[\begin{array}{cccc} P(w_{1}|+)& P(w_{2}|+) & \cdots &P(w_{k}|+)\end{array}\right].
$$
$$
P_{-} = \frac{1}{N_{-}}(1-Y)^{\intercal}X =  \left[\begin{array}{cccc} P(w_{1}|-)& P(w_{2}|-) & \cdots &P(w_{k}|-)\end{array}\right].
$$

\vfill\eject
## Likelihood

$$
P(f|\pm) = \prod_{i: f_{i}=1} P(w_{i}|\pm)\prod_{i: f_{i}=0}(1-P(w_{i}|\pm))
$$
$$
P(f|\pm) = \prod_{i=1}^{k} P(w_{i}|\pm)^{f_{i}}(1-P(w_{i}|\pm))^{(1-f_{i})}.
$$

- Log likelihood is simpler to work with

$$
\log P(f|\pm) = \sum_{i=1}^{k} f_{i}\log P(w_{i}|\pm) + (1-f_{i})\log(1-P(w_{i}|\pm))
$$

\vskip 1in
#### Matrix form


$$
\log P(X|\pm) = X(\log P_{\pm})^{\intercal}+(1-X)(\log (1-P_{\pm}))^{\intercal}.
$$

\vskip 1in
#### Bayes Theorem

$$
\log P(\pm|f) = \log P(f|\pm)+\log P(\pm) - \log P(f)
$$

\vskip 1in
#### Decision rule

- a review is positive if $\log P(f|+)+\log P(+)>\log P(f|-)+\log P(-)$ and negative otherwise.
