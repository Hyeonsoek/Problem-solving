#include <cstdio>
int input[51],check[51];
int N,num,root,cnt;
int dfs(int K) {
	check[K] = 1;
	int a = 1;
	for (int i=0;i<N;i++) {
		if(i!=num&&input[i]==K&&!check[i]) {
			a = 0;
			dfs(i);
		}
	} if (a) cnt++;
}
int main() {
	scanf("%d",&N);
	for(int i=0; i<N; i++) {
		scanf("%d",&input[i]);
		if (input[i]==-1) root=i;
	} scanf("%d",&num);
	if (num!=root)
		dfs(root);
	printf("%d",cnt);
}
