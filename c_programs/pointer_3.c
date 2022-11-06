#include <stdio.h>

int main(){

    int myNumber = 15;
    int* ptr = &myNumber;

    printf("My number is %d\n", myNumber);
    printf("My number memory address is %p\n", ptr);

    // // Dereference: Output the value of number with the pointer 
    printf("My number is %d\n", *ptr);

    return 0;
}