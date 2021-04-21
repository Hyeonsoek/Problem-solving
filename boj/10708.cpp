#include <cstdio>
int main() {
	int n,m,t[101]={},m[101][101],p[101]={};
	scanf("%d%d",&n,&m);
	for(int i=0; i<m; i++)
		scanf("%d",&t[i]);
	for(int i=0; i<m; i++) {
		for(int j=0; j<n; j++)
			scanf("%d",&m[i][j]);
		int c=0;
		p[taget[i]-1]++;
		for(int j=0; j<n; j++) {
			if(j!= t[i]-1) {
				if(m[i][j]==t[i]) p[j]++;
				else c++;
			}
		}p[t[i]-1]+=c;}
	for(int i=0; i<n; i++)
		printf("%d\n",p[i]);
}