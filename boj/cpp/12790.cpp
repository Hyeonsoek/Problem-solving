#include <cstdio>

int main() {
	int T;
	for(scanf("%d",&T);T--;) {
		int last = 0;
		int HP,MP,attack,sheild;
		int upHP,upMP,upattack,upsheild;
		scanf("%d%d%d%d",&HP,&MP,&attack,&sheild);
		scanf("%d%d%d%d",&upHP,&upMP,&upattack,&upsheild);
		HP += upHP,MP += upMP;
		attack += upattack, sheild += upsheild;

		last = 1*(HP < 1 ? 1 : HP) + 5*(MP < 1 ? 1 : MP) + 2*(attack < 0 ? 0 : attack) + 2*sheild;
		printf("%d\n",last);
	}
}