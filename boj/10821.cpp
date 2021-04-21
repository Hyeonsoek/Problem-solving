#include <cstdio>
#include <string>
#include <iostream>
using namespace std;
int main(){
	string input;
	cin >> input;
	int count=0,len = input.size();
	const char *cstr = input.c_str();
	for (int i = 0; i < len; i++) {
		if (i == 0 && cstr[i] == ',') continue;
		if (cstr[i] == ',' && (cstr[i-1]>='0' && cstr[i-1] <= '9')) {
			count++;
		}
	} printf("%d",count+1);
}
