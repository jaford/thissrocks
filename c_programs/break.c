#include <stdio.h>

int main(){

    int i;

    // i++ is our counter?
    // i sets the int to start at 0
    // i is stating that i is less than 10
    for (i = 0; i < 10; i++) {
        if(i==4) {
            // This will break off the loop. 
            // AKA jump out of the loop
            break;
        }
        printf("%d\n", i);
    }
    return 0;
}