#include <string>
#include <iostream>
using namespace std;

int main()
{
	string str;
	getline(cin,str);
	while(str != "END")
	{
		int len = str.size();
		for(int i=1; i<=len; ++i)
			cout << str[len-i];
		cout << endl;
		getline(cin,str);
	}
}