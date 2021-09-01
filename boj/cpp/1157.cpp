#include <stdio.h>
#include <string.h>
int str[1000001];
int alpha[27] = {};
int main()
{
    scanf("%s",str);
    int len = 200;
    for (int i = 0; i < len; i++) {
        if (str[i] >= 'a' && str[i] <= 'z')
            alpha[str[i] - 'a']++;
        if (str[i] >= 'A' && str[i] <= 'Z')
            alpha[str[i] - 'A']++;
    }
    int idx, cnt = 0, max = alpha[0];
    for (int i = 1; i < 27; i++) {
        if (alpha[i] == max) {
            cnt++;
        }
        if (alpha[i] > max) {
            max = alpha[i];
            idx = i;
            cnt = 0;
        }
    }
    if (cnt > 0)
        printf("?");
    else
        printf("%c", 'A' + idx);
}
