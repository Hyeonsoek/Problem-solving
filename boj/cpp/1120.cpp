#include <iostream>
#include <string>
using namespace std;

int XandY(string X,string Y)
{
	int ret = 0;
	int xSize = X.size();
	for(int i=0; i<xSize; ++i)
		if(X[i] != Y[i])
			++ret;
	return ret;
}

int main()
{
	string A,B;
	cin >> A >> B;
	int m = 51;
	for(int i=0; i<=B.size()-A.size(); ++i)
		m = min(m,XandY(A,B.substr(i,A.size())));
	cout << m;
}