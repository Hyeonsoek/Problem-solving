#include <cstdio>
int main() {
	int a,b,x,y;
	scanf("%d%d%d%d",&a,&b,&x,&y);
	if (a < x-a && b < y-b) {
		if (b < a) printf("%d",b);
		else printf("%d",a);
	}
	else if (a >= x-a && b < y-b) {
		if (b < x-a) printf("%d",b);
		else printf("%d",x-a);
	}
	else if (a < x-a && b >= y-b) {
		if (y-b < a) printf("%d",y-b);
		else printf("%d",a);
	}
	else if (a >= x-a && b >= y-b){
		if (x-a < y-b) printf("%d",x-a);
		else printf("%d",y-b);
	}
}
