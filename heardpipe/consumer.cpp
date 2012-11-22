#include <iostream>

int main() {
    double num;
    double total=0;
    size_t lines=0;
   // std::cout<<"HELLO"<<std::endl;
    while(std::cin >> num) {
   // std::cout<<total<<std::endl;
	total += num;
	++lines;
    }
    std::cout << total << "/" << lines << "=" << total/lines << std::endl;
}
