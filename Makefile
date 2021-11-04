all:
	xelatex main.tex
	xelatex main.tex
	rm -f main.log main.aux main.out
clean:
	rm -f main.log main.aux main.out
