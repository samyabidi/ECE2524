
all: paper1.html paper1.pdf preview

paper1.html: paper1.md
	pandoc paper1.md -o paper.html
	
paper1.pdf: paper1.md
	pandoc -o paper1.pdf paper1.md

preview: paper1.md
	less paper1.md
