#include <cstdio>
int self[10001];
int selfnum(int num) {
	if (num < 10) {
		return num+num;
	} else if (num >= 10 && num <100) {
		return num/10+num%10+num;
	} else if (num >= 100 && num <1000) {
		return num/100+(num%100)/10+(num%100)%10+num;
	} else {
		return num/1000+(num%1000)/100+((num%1000)%100)/10+((num%1000)%100)%10+num;
	}
}
int main() {
	for (int i = 1; i<=10000; i++) {
		if (!self[i]) {
			printf("%d\n",i);
			self[selfnum(i)]=1;
			for (int j=selfnum(i); j=selfnum(j),j<=10000;) {
				self[j] = 1;
			}
		}
	}
}
