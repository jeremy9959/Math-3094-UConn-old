# Course outline

See [this page](LabResources.html) for help on Anaconda, Jupyter, and Python.

## Part One

### Linear Regression (1/18/21-1/29/21)

Goals 

- Learn the mathematics of Linear Regression (ordinary least squares) using Linear Algebra

	- [Simple Linear Regression](https://www.youtube.com/watch?v=81pbJqQQa5M&list=PLHmPFY5Rz0RCWU4ra8aqBM7AvrGdPDOhR&index=1)
	- [Linear Regression - Geometry](https://www.youtube.com/watch?v=55FFmKh4CXg&list=PLHmPFY5Rz0RCWU4ra8aqBM7AvrGdPDOhR&index=2)
	- [Multivariate Regression - Introduction](https://www.youtube.com/watch?v=pqCEgpep_2w&list=PLHmPFY5Rz0RCWU4ra8aqBM7AvrGdPDOhR&index=3)
    - [Multivariate Regression - Calculus](https://www.youtube.com/watch?v=_-HrPrkpsjY&list=PLHmPFY5Rz0RCWU4ra8aqBM7AvrGdPDOhR&index=4)
	- [Multivariate Regression - Geometry](https://www.youtube.com/watch?v=E3hyjNeD9AA&list=PLHmPFY5Rz0RCWU4ra8aqBM7AvrGdPDOhR&index=5)
	- [Multivariate Regression - Centered Coordinates](https://www.youtube.com/watch?v=mTasFUNob54&list=PLHmPFY5Rz0RCWU4ra8aqBM7AvrGdPDOhR&index=7)
	
- Lab: 
	- get a working installation of anaconda, python, and jupyter on your computer.
	- a basic introduction to working with  the Jupyter notebook
	- fundamentals of Python
	- calculations and plotting examples of linear regression

*References*


- Linear Regression [html](published_notes/notes/LR.html)  [pdf](published_notes/notes/LR.pdf)
- Linear Regression lab - includes datafiles and ipynb file. [zip](published_notes/notes/RegressionLab.zip) [tgz](published_notes/notes/RegressionLab.tgz)
- See also [the Lab Resources page](LabResources.md) for help.

### Gradient Descent (2/2/21 - 2/12/21)

Goals:

- Learn the basic theory of gradient descent and how it is applied to find maxima and minima of functions
- Apply Gradient Descent to some specific examples.
- Learn Newton's method and apply it to some examples.

	- [Introduction to Binary Classification](slides/intro-bin-class.pdf)
	- [Gradient Descent](slides/grad-descent.pdf)
    - [Newton's Method](slides/Newton-method.pdf)

*References*

- Gradient Descent [html](published_notes/notes/GD.html) [pdf](published_notes/notes/GD.pdf)
- Gradient Descent lab - includes datafiles and ipynb file. [zip](published_notes/notes/GradientDescentLab.zip) [tgz](published_notes/notes/GradientDescentLab.tgz) 

### Probability

Goals:

- Get an introduction to the key ideas from probability that play a role in machine learning.
- Learn about mean, variance, independence, conditional probability, and Bayes theorem.
- Try out the Naive Bayes classification method
- Introduce the ideas of statistical models and maximum likelihood.

- [Probability Basics](https://www.youtube.com/watch?v=7RH04w7dWp0&list=PLHmPFY5Rz0RDVDokDgADG9CfmBhwZLF9M&index=1)
- [Conditional Probability 1](https://www.youtube.com/watch?v=7RH04w7dWp0&list=PLHmPFY5Rz0RDVDokDgADG9CfmBhwZLF9M&index=2)
- [Conditional Probability 2](https://www.youtube.com/watch?v=7RH04w7dWp0&list=PLHmPFY5Rz0RDVDokDgADG9CfmBhwZLF9M&index=3)
- [Probability - Independence](https://www.youtube.com/watch?v=7RH04w7dWp0&list=PLHmPFY5Rz0RDVDokDgADG9CfmBhwZLF9M&index=4)
- [Probability - Random Variables 1](https://www.youtube.com/watch?v=7RH04w7dWp0&list=PLHmPFY5Rz0RDVDokDgADG9CfmBhwZLF9M&index=5)
- [Probability - Random Variables 2](https://www.youtube.com/watch?v=7RH04w7dWp0&list=PLHmPFY5Rz0RDVDokDgADG9CfmBhwZLF9M&index=6)
- [Probability - Expectation and Variance](https://www.youtube.com/watch?v=7RH04w7dWp0&list=PLHmPFY5Rz0RDVDokDgADG9CfmBhwZLF9M&index=7)
- [Probability - Statistical Models](https://www.youtube.com/watch?v=7RH04w7dWp0&list=PLHmPFY5Rz0RDVDokDgADG9CfmBhwZLF9M&index=8)

*References*

- Probability Notes [html](published_notes/notes/Probability.html) [pdf](published_notes/notes/Probability.pdf)
- Naive Bayes Notes [html](published_notes/notes/NaiveBayes.html) [pdf](published_notes/notes/NaiveBayes.pdf)
- Naive Bayes Lab - includes datafiles and ipynb file. [zip](published_notes/notes/naive_bayes.zip) [tgz](published_notes/notes/naive_bayes.pdf)

### Logistic Regression

Goals: 

- Understand the statistical model underlying logistic regression
- See how the ideas of likelihood and gradient descent combine to solve the logistic regression problem
- Do some sample computations to see Logistic Regression in action
- Generalize binary logistic regression to multi-class logistic regression
    - [Logistic Regression](slides/logistic-regression.pdf)
    - [Multi-class Logistic Regression](slides/multi-LR.pdf)

*References*

- Logistic Regression [html](published_notes/notes/LogitR.html) [pdf](published_notes/notes/LogitR.pdf)
- Logistic Regression lab - includes datafiles and ipynb file. [zip](published_notes/notes/LogitRegLab.zip) [tgz](published_notes/notes/LogitRegLab.tgz) 

### Principal Component Analysis

Goals:

- Learn about how the covariance matrix encodes variation in linear combinations of features
- Learn the correlation coefficient
- Understand principal components and their relationship to eigenvectors of the covariance matrix
- See how to use principal components for dimension reduction.
- Do some examples.

- [Variance, Covariance, Correlation, and the Covariance Matrix](https://youtu.be/WrYCUQWO0NE)
- [Scores](https://youtu.be/rhr2Le7-OPM)
- [Geometry of Scores](https://youtu.be/TmIr5lg4i4k)
- [Principal Directions - First Look](https://youtu.be/ZydwxPG0_o8)
- [Finding the Principal Directions](https://youtu.be/x9Nu10WF6lg)
- [The Spectral Theorem](https://youtu.be/_vxLZ1M8xr8)
- [Dimension Reduction](https://youtu.be/tOWBQEQ9qpI)
- [Loadings](https://youtu.be/hdxPdIrfF2s)

*References*

- Principal Component Analysis [html](published_notes/notes/PCA.html) [pdf](published_notes/notes/PCA.pdf)
- PCA Lab -- includes notebook(s) and data [zip](published_notes/notes/PCALab.zip) [tgz](published_notes/notes/PCALab.tgz)



### Bayesian Regression

Goals:

- Learn the process of Bayesian inference (see also the notes on probability above).
  - [Intro to Bayesian Inference](https://youtu.be/sk1elwY_Ggo)
  - [Bayesian Coin Flipping](https://youtu.be/NHfQ_88y0CE)
- Understand over-fitting in linear regression
- Study Bayesian linear regression
- Understand the ideas of linear discriminant analysis
    - [Bayesian Linear Regression](slides/bayesian-lin-reg.pdf)
    - [Linear Discriminant Analysis](slides/LDA.pdf)
    - [Dimensionality Reduction via LDA](slides/dim-red-LDA.pdf)

*References*

- Bayesian Regression Lab -- includes notebook(s) and data [zip](published_notes/notes/bayesian-regression.zip) [tgz](published_notes/notes/bayesian-regression.tgz)


### Support Vector Machines


Goals:

- Learn the ideas behind support vector machine classifiers
  - [Introduction](https://youtu.be/-mFZChnwTdQ)
  - [Optimal Margins](https://youtu.be/VOCaNMTyCdQ)

- Understand the relationship between convex hulls, supporting hyperplanes, and support vector machines
  - [Convexity, Convex Hulls, and Supporting Hyperplanes](https://youtu.be/voOt3bv0Vng)

- Formulate the convex optimization problem yielding the optimal margin classifier
  - [Closest Points and Optimal Margins 1](https://youtu.be/N4APHjxTObs)
  - [Closest Points and Optimal Margins 2](https://youtu.be/DaF6PhZ6EaA)
  - [Formulating the Optimization Problem](https://youtu.be/BB2NwZsPvaI)
  
- Learn the sequential minimum optimization algorithm
  - [The SMO Algorithm](https://youtu.be/xsuyqXwCXRk)
  
- Further ideas
  - [Kernels, inseparable sets, multiclass classification](https://youtu.be/xsuyqXwCXRk)


*References:*

- Notes on support vector machines [html](published_notes/notes/SVMNotes.html) [pdf](published_notes/notes/SVMNotes.pdf)
- Support Vector Machines Lab (includes jupyter notebook and data files) [zip](published_notes/notes/SVMLab.zip) [tgz](published_notes/notes/SVMLab.tgz)


### Neural Networks 

Goals:

- Learn the ideas of neural networks and understand forward-propagation and back-propagation
- Derive the back-propagation formula
- Learn the mechanisms of basic convolutional neural networks
    - [Basic Neural Networks](slides/basic-neural-networks.pdf)
    - [Convolutional Neural Networks](slides/cnn.pdf)

*References*

- Neural Networks Lab -- includes notebook(s) and data [zip](published_notes/notes/neural-networks.zip) [tgz](published_notes/notes/neural-networks.tgz)


