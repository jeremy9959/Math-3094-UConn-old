# Overview of class

Each week has classes on Tuesday and Thursday. On Tuesdays, give lectures on mathematical theory;
on Thursdays, at least in the half of the semester, have lab-days to work on data sets through computer coding and packages. 


### Topics to cover
This is a list of topics that should be discussed somehow during the course

### Introductory topics (1 week)
- Math Topics
  - What is machine learning?
  - what is supervised learning w/examples
  - what is unsupervised learning w/examples
  - Cases:
	- classification
	- regression
	- clustering
   - Data
	- features
	- samples
   - categorical and real variables
   - mean and variance


- Programming
  - Python introduction
  - jupyter notebooks
	- self-documenting code and markdown
	- plotting
  - scikit-learn introduction
  - plotting

### Linear Regression (1 week)

- Math

	- Geometry of linear regression
	By this I mean the problem of finding the line or hyperplane or hyperspace minimzing squared error
	without any probability in the background

  

- Programming
	
	- Do a linear regression problem
	- Illustrate overfitting/underfitting with polynomial regression
    - Exponential fitting 


### PCA/SVD (1 week)

- Math
  - The covariance matrix and variance of data along different axes
  - Recall theory of definite binary quadratic forms and geometric interpretation (ellipsoids)
  - Principal directions  and the optimization problem
  - Eigenvalues, eigenvectors, and principal directions
  - Projection of data into lower dimensional spaces spanned by eigenvalues
  - Clustering data in the low dimensional space (K-means, Nearest Neighbors)
  - Loadings of original features (projection of feature directions into principal component space)

- Programming
  - Work through PCA for simulated data to reveal clustering


### Optimization (1 week)

- Math

	- Use ridge regression as an example to discuss
		- convex optimization
		- Gradient Descent
	
- Programming

	- explore effect of tuning parameter
	


### Multivariate Gaussian (1 week)

- Math
	- Introduce the normal and multivariate normal distribution, covariance matrix

	- Probabilistic model of linear regression and MLE
	Redo linear regression in terms of the linear model.
	Here we talk about the linear model that says Y = aX+b+epsilon where epsilon is a normally distributed
	error term and we interpret a, b as MLE estimates. 

	- Look again at PCA in the context of the multivariate gaussian distribution.

- Programming

	- 
	
### Logistic Regression (1 week)

- Math

	- the logistic model 
	- the likelihood of the data and MLE
	- gradient descent
	- LR as a classifier
	
- Programming

	- programming gradient descent in the one dimensional case? 
	- higher dimensional case?
	- example application, perhaps to image data (MNIST)?
	

### Some Bayesian ideas (1 week)

- Math

	- precision, recall, sensitivity, specificity and conditional probability
	- the ROC curve
    - Bayes theorem, prior knowledge, and posterior knowledge
	- coin flipping and the beta distribution
	
- Programming

	- ROC curve examples
	- metric examples (precision, recall, etc)
	- coin flipping simulations
	

### More Bayesian Ideas (1 week)

- Math
  - Bayesian normal(?) with conjugate prior?
  - Bayesian linear regression (simple cases) and the likelihood
  
- Programming

   - simulations
   - monte carlo methods
   - sampling and bayesian linear regression
   - naive bayes classifier (spam filter)


### Support Vector Machines (1 week)

- Math
  - geometry of SVM
  - optimization with inequalities (Lagrange multipliers/KKT theorem)
  - linearly separable data
  - approximate svm
  - kernels and svm 

- Programming
  - SVM classifier example
  
### Clustering (1 week)

- Math
  - Hierarchical clustering and linkage 
  - K-means
  

### Introduction to Neural Networks (2 weeks)
- Math
  - LR as a neural network
  - computation graphs and activation functions
  - the multi-layer perceptron
  - forward and back-propagation and gradient descent
  
- programming
 - experiments with images (MNIST)


   
\end{enumerate}


\end{document}
