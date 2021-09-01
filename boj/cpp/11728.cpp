#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
    int N,M,K;
    vector<int> a;
    scanf("%d%d",&N,&M);
    K = N + M;
    for(int i=0; i<N+M; i++) {
        int input;
        scanf("%d",&input);
        a.push_back(input);
    } sort(a.begin(),a.end());
    for(int i=0; i<N+M; i++) {
        printf("%d ",a.at(i));
    }
}
