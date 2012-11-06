#makefile for makemake
Wall    = 

all: exprtest

exprtest: exprtest.o driver.o parser.tab.o scanner.o
	g++ ${Wall} -g -o exprtest exprtest.o driver.o parser.tab.o scanner.o

driver.o: driver.cpp driver.hpp scanner.hpp parser.tab.hpp stack.hh \
 location.hh position.hh
	g++ ${Wall} -g -c driver.cpp

exprtest.o: exprtest.cpp driver.hpp expression.hpp
	g++ ${Wall} -g -c exprtest.cpp

parser.tab.o: parser.tab.cpp expression.hpp parser.tab.hpp stack.hh \
 location.hh position.hh driver.hpp scanner.hpp
	g++ ${Wall} -g -c parser.tab.cpp

scanner.o: scanner.cpp scanner.hpp parser.tab.hpp stack.hh location.hh \
 position.hh
	g++ ${Wall} -g -c scanner.cpp 

parser.tab.cpp: parser.ypp
	bison parser.ypp

parser.tab.hpp: parser.ypp
	bison parser.ypp

scanner.cpp: scanner.ll
	flex -t scanner.ll > scanner.cpp
	
clean:
	rm -f *.o core
	rm -f exprtest
	rm -f scanner.cpp
	rm -f location.hh
	rm -f parser.tab.cpp
	rm -f parser.tab.hpp
	rm -f position.hh
	rm -f stack.hh

    

