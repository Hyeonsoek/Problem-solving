#include <stdio.h>
int gcd(int a,int b) {
	int temp = 1,gcd = -1;
	while(temp <= a || temp <= b) {
		if (!(a%temp)&&!(b%temp)&&gcd < temp) {
			gcd = temp;
		}
		temp++;
	}
	return gcd;
}

int main() {
    int n,i,a,b,c,d,e,f;
	scanf("%d%d",&a,&b);
	f = gcd(a,b);
    d=a,e=b;
    while (b!=0) {
		c = a;
        a = b;
    	b = c%b;
    }
    printf("%d\n%d",f,(d*e)/a);
}
