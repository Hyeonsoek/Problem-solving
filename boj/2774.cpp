#include <cstdio>
#include <string>
using namespace std;
int main() {
	int N;
	for (scanf("%d",&N);N--;) {
		int input,count[11]={},m=0;
		scanf("%d",&input);
		string s = to_string(input);
		for (int i = 0; i < s.size(); i++) {
			count[s[i]-'0']++;
		}
		for (int i = 0; i < 10; i++) {
			if (count[i]>0) m++;
		} printf("%d\n",m);
	}
}
