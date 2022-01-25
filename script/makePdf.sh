sudo docker exec -it pdfMaker /bin/bash -c "texliveonfly main.tex --compiler=xelatex ; latexmk -pdfxe main.tex"
