paper: main.md
	pandoc -N --standalone   --filter pandoc-secnos --filter pandoc-fignos --filter pandoc-eqnos --filter pandoc-citeproc  -t latex -o main.tex main.md

pdf: paper
	pdflatex main.tex
	pdflatex main.tex

html: main.md
	pandoc -N --standalone --mathjax --filter pandoc-secnos --filter pandoc-fignos --filter pandoc-eqnos --filter pandoc-citeproc   -t html -o main.html main.md
