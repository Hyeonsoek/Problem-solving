#include <cstdio>
#include <stack>
using namespace std;
stack<int> s;
int main() {
	int N,sum=0;
	for (scanf("%d",&N);N--;){
		int num;
		scanf("%d",&num);
		if (num!=0) {
			sum+=num;
			s.push(num);
		} if (num==0) {
			sum-=s.top();
			s.pop();
		}
	} printf("%d",sum);
}
