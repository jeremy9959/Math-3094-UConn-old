---
title: Linear Regression
author: Jeremy Teitelbaum
fontsize: 12pt
---

# Linear Regression 

## Introduction

Linear regression is a prototypical machine learning algorithm.   To get a feel
for it, let's look at some data on the relationship between engine size and gas mileage
for a group of cars (see [UCI-auto-mpg] or, for a nicely formatted csv version, 
[kaggle-auto-mpg]).

In its simplest
version, we start with the assumption that a particular quantity $y$ that we would like
to understand depends on a quantity $x$ that we know through a linear relationship:
Also, we have $x\in\R$.

For example, look at 

![Miles Per Gallon vs Engine Displacement][mpg-vs-displacement]\ 

<!--
images
-->


[mpg-vs-displacement]: ../img/mpg-vs-displacement.png 




<!--
links
-->
[kaggle]: http://www.kaggle.com
[kaggle-auto-mpg]: https://www.kaggle.com/uciml/autompg-dataset
[UCI]: https://archive.ics.uci.edu/ml/index.php
[UCI-auto-mpg]: https://archive.ics.uci.edu/ml/datasets/Auto+MPG
