paper: main.md 
	pandoc -N --listings --standalone  --filter pandoc-tablenos --filter pandoc-secnos --filter pandoc-fignos --filter pandoc-eqnos  --citeproc  -t latex -o main.tex main.md


pdf: paper
	pdflatex main.tex
	pdflatex main.tex

html: main.md 
	pandoc -N --standalone --mathjax  --filter pandoc-tablenos --filter pandoc-secnos --filter pandoc-fignos --filter pandoc-eqnos --citeproc   -t html -o main.html main.md

