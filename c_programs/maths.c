#include <stdio.h>

int main(){

    int mynum1 = 50 + 50;
    int mynum2 = mynum1 - 25;
    int mynum3 = mynum2 * 2;
    int mynum4 = mynum3 / 2;

    printf("%d\n", mynum4);

    // Sizeof Operator
    // The memory size (in bytes) of a data type or a variable 
    // can be found with the sizeof operator
    printf("%lu\n", sizeof(mynum4));
    return 0;
}