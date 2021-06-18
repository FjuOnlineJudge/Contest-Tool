all:
	xelatex main.tex
	xelatex main.tex

clean:
	rm -f main.log main.aux main.out
