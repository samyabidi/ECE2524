CXX := g++-4.7
CPPFLAGS := -Wall -g -std=c++11

all: process-test consumer

process-test: process-test.o Process.o Process.h
	$(CXX) $(CPPFLAGS) -o $@ $^

consumer: consumer.o
	$(CXX) $(CPPFLAGS) -o $@ $^


clean:
	-rm -f *.o
