### The MNIST classification problem

To provide a concrete example, we will introduce one of the most famous data sets in the machine learning
world -- the [MNIST](http://yann.lecun.com/exdb/mnist/) set of handwritten digits.  
[Originally developed](https://www.nist.gov/system/files/documents/srd/nistsd19.pdf) by
the [National Institute of Standards and Technology](https://www.nist.gov) to help
test methods for automated reading of ZIP codes and other problems of optical character recognition,
the data was cleaned up, organized, and distributed by [Yann LeCun](http://yann.lecun.com/)
for use by machine learning researchers.

This data set consists of 60 thousand examples of handwritten digits from $0$ to $9$, each
represented as a $28\times 28$ grid of "pixels."  Each pixel has a value between $0$ and $255$
representing how dark that particular pixel is in that image.  So a value of zero means that
cell is black, and a value of 255 means it's white.   Here are some examples (with thanks
to @mnistexamples).

![MNIST Examples](../img/MnistExamples.png){#fig:mnist-examples}

From the point of view of a machine learning algorithm, each $28\times 28$ matrix of integers
can be thought of as a $28\times 28=784$ dimensional vector of numbers between $0$ and $255$.
And a collection of $n$ such digits can be organized into an $n\times 784$ dimensional data
matrix $X$.  In the MNIST dataset, each image comes with a label from $0$ to $9$ which says
what the particular handwritten digit actually *is*.

The MNIST classification problem is then to develop an algorithm whose input is a $784$ dimensional
vector and whose output is a number from $0$ to $9$.  In that sense, this classification problem
is a kind of regression -- we want to compute the label from the data. But in this situation, the
labels are a discrete set and something like linear regression makes no sense.
