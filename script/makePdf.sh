docker compose up -d
docker exec -it pdfmaker bash -c "xelatex problem.tex"
docker compose down -v
rm problem.[^tp]*