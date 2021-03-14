

%.html : %.md
	pandoc -s --mathjax -t slidy $< -o $@

#%.pdf : %.md
#	pandoc -s --slide-level=2 --variable classoption=t --mathjax -t beamer $< -o $@

%.pdf : %.md
	pandoc -s --filter pandoc-xnos -o $@ $<
