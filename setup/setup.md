# Setup

## Software

We will use `pandoc` and an associated set of extensions called `pandoc-xnos`.  See the
`pandoc` and `pandoc-xnos` documentation for installation instructions.

We also use the UNIX utility `make`.

The python code relies on `numpy`, `sklearn`,`pandas`, and the `bokeh` visualization library, as well
as on the `jupyter` notebook ecosystem.


## Directory Structure

0.  The main Github repo has subdirectories

- `references` that contains a BiBTeX file of references for the notes
- `resources` containing various configuration files (for now, the .csl file that sets a citation style)
- `data` contains datasets used in the notes

1.  Each Chapter is in an appropriately named subdirectory of the main Github repo.


2.  Inside that subdirectory are further subdirectories:

- `notes` holds the markdown file and the various files that are created by pandoc
- `src` holds python code or other code for generating figures
- `lab` holds the .ipynb files for the lab assignments
- `img` holds the .png files for the images
- `data` holds any data files for generating images or for the labs -- probably this should be merged into
the project-wide data directory.


## Markdown and pandoc

Each chapter is written in the `pandoc` dialect of markdown in a file called `main.md`.

The file begins with some configuration settings:

```yaml
--- 
pagetitle: Linear Regression 
colorlinks: true 
linkcolor: blue
link-citations: true 
csl: [../../resources/stat.csl]
bibliography: [../../references/references.bib]
reference-section-title: References 
xnos-cleveref: True 
---
```

LaTeX macros can be included after this configuration block and used throughout the rest of the file.

TeX is embedded in the markdown following usual conventions, with dollar signs and double-dollar signs
for in-line and displayed math as usual.  Here is a sample:

```
In either of the two cases above, the question we face is to determine
the line $y=mx+b$ that "best fits" the data $\{(x_i,y_i)_{i=1}^{N}\}$.
The classic approach is to determine the equation of a line $y=mx+b$
that minimizes the "mean squared error":

$$ MSE(m,b) = \frac{1}{N}\sum_{i=1}^{n} (y_i-mx_i-b)^2 $$

It's worth emphasizing that the $MSE$ is a function of two variables
-- the slope $m$ and the intercept $b$ -- and that the data points
$\{(x_i,y_i)\}$ are constants for these purposes.  Furthermore, it's a
quadratic function in those two variables.  Since our goal is to find
$m$ and $b$ that minimize the $MSE$, we have a Calculus problem that
we can solve by taking partial derivatives and setting them to zero.
```

## References

### Sections

Headings can be labelled with `{#sec:label}` like this:

```
## Least Squares (via Calculus) {#sec:Calculus}
```

and then referred to like this:

```
See +@Calculus for a discussion ....
```

### Figures

Figures are included (and labelled) like this:

```
![Distance to A Plane](../img/distance-to-plane.png){#fig:perp width=50%}
```

This can be referred to as follows:

```
See +@fig:perp for a picture of the situation
```

and it will have `Distance to a Plane` as a caption.

### Equations

Equations can be labelled like this:

```
$$ \begin{aligned} m(X\cdot E) &+ b(E\cdot E) &= (Y\cdot E) \cr
m(X\cdot X) &+ b(E\cdot X) &= (Y\cdot X) \cr \end{aligned}
$${#eq:LSAnswer2}
```

and referred to like:

```
See +@LSAnswer2 for the equation.
```

### Citations

Referring to `@key` where key is one of the bibtex keys generates a reference to a citation.

For example:

```
See @irvine for the mpg dataset.
```


## Processing

The advantage of starting from `pandoc markdown` is that you can generate both `pdf` and
`html` and preserve the references and equation numbers and so on. In fact, you generate TeX which
then becomes pdf.  The command to generate html is:

```bash
$ pndoc -N --standalone --mathjax --filter pandoc-secnos --filter pandoc-fignos --filter pandoc-eqnos --filter pandoc-citeproc   -t html -o main.html main.md
```

The command to generate TeX is

```bash
$ pandoc -N --standalone   --filter pandoc-secnos --filter pandoc-fignos --filter pandoc-eqnos --filter pandoc-citeproc  -t latex -o main.tex main.md
```

Then you need to run `pdflatex` (twice) to create the pdf file (and get the references right):

```bash
$ pdflatex main
$ pdflatex main
```

You can preview the html by opening the file in a web browser, and the pdf by using a pdf viewer.


### make

`make` is a utility that can simplify this a little bit.  If this [Makefile](./Makefile) is located
in the notes directory, and your main markdown file is called `main.md`, then you can just type:

```
$ make html
```

to generate the html file and

```
$ make pdf
```

to generate the pdf file. 
