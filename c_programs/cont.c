#include <stdio.h>

int main(){

    int i; 

    for (i = 0; i < 20; i++) {
        if(i==4) {
            // This continues the count even if the if i is 4
            continue;
        }
        printf("%d\n", i);
    }
    return 0;
}
