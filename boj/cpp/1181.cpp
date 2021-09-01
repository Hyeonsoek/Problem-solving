#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

bool cmp(string &a, string &b) {
	if(a.length() == b.length())
		return a < b;
	return a.length() < b.length();
}

int main() {
	vector< string > v;
	int n;
	scanf("%d",&n);
	for(int i=0; i<n; i++) {
		int bo=0;
		string s;
		cin >> s;
		for(int i=0; i<v.size(); i++) {
			if(s == v[i]) {
				bo = 1;
				break;
			}
		}
		if(bo == 0)
			v.push_back(s);
	}

	sort(v.begin(),v.end(),cmp);
	for(int i=0; i<v.size(); i++)
		cout << v[i] << '\n';
}
