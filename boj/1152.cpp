#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;
int main() {
	string A;
	getline(cin,A);
	const char* input = A.c_str();
	int size = A.size(),count=0,fuck=0;
	for (int i = 0; i <size; i++) {
		if (input[i] == 32 && (i == 0 || i == size-1)) fuck++;
		if (input[i] == 32 && input[i-1] == 32) fuck++;
		if (input[i] == 32) count++;
	}
	if (count == size) printf("0");
	else printf("%d",count+1-fuck);
}
