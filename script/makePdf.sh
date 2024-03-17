docker-compose exec pdfMaker bash -c "texliveonfly problem.tex --compiler=xelatex ; latexmk -pdfxe problem.tex"
rm -f problem.[^tp]* missfont.log
