#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
	vector< string > v;
	string input;
	cin >> input;
	for(int i=0; i<input.size(); i++) {
		v.push_back(input.substr(i,input.size()-i));
	} sort(v.begin(),v.end());
	for(int i=0; i<v.size(); i++) {
		cout << v.at(i) << "\n";
	}
}
