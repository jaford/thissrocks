#include <stdio.h>


int main() {

    int myNum = 10;

    printf("%p", &myNum); 
    // This prints the result of whatever your variable is in hexadecimal.
    // When a variable is made, a memory address is assigned. 
    // You can view the address in the line above! 

    return 0;
}