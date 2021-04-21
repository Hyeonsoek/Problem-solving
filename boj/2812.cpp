#include <cstdio>
#include <stack>
using namespace std;

int main()
{
	int N,K;
	char input[500010]={};
	scanf("%d%d%s",&N,&K,input);

	stack<char> s;
	s.push(input[0]);

	for(int i=1; i<N; ++i)
	{
		while(!s.empty() && s.top() < input[i] && K)
			{ s.pop(); --K; }
		s.push(input[i]);
	}

	while(K--) s.pop();

	int cnt = 0;
	char ret[500010] = {};
	while(!s.empty())
	{
		ret[cnt++] = s.top();
		s.pop();
	}
	for(int i=cnt-1; i>-1; --i)
		printf("%c",ret[i]);
}