docker unpause pdfMaker
docker exec -it pdfMaker bash -c "texliveonfly problem.tex --compiler=xelatex ; latexmk -pdfxe problem.tex"
docker pause pdfMaker
rm problem.[^tp]* texput.log