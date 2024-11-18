#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    int n;
    int a[100];
    scanf("%d", &n);
    for(int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }
    int f;
    scanf("%d", &f);
    
    int c = 0;
    for(int i = 0; i < n; i++) {
        if(a[i] == f) {
            c += i;
            break;
        }
    }
    if(c == 0) {
        printf("-1");
    }
    else {
        printf("%d", c);
    }
    
    return 0;
}
