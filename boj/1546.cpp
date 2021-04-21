#include <cstdio>

int main() {
	int n;
	float max=-1,sum=0,arr[1001];
	scanf("%d",&n);
	for(int i=0; i<n; i++) {
		scanf("%f",&arr[i]);
		if(arr[i] > max)
			max = arr[i];
	}

	for(int i=0; i<n; i++) {
		arr[i] = (arr[i]/max)*100;
		sum += arr[i];
	}
	printf("%.2f",(float)(sum/((float)(n))));
}