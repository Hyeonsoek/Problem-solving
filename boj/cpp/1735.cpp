#include <cstdio>
int main() {
	int A,B,C,D;
	scanf("%d%d%d%d",&A,&B,&C,&D);
	int temp_1 = B,temp_2 = D;
	while (temp_2 != 0) {
		int E = temp_1;
		temp_1 = temp_2;
		temp_2 = E % temp_2;
	}
	int LCM = (B*D)/temp_1;
	A *= LCM/B;
	C *= LCM/D;
	int fract = A + C;
	temp_1 = fract,temp_2 = LCM;
	while (temp_2 != 0) {
		int E = temp_1;
		temp_1 = temp_2;
		temp_2 = E % temp_2;
	} fract /= temp_1,LCM /= temp_1;
	printf("%d %d",fract,LCM);
}
