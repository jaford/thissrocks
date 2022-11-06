#include <stdio.h>

int main(){

    int myNumber = 10;
    // This is assigning the address to a variable. (AKA pointer) 
    int* ptr = &myNumber;

    printf("Here is my number %d\n", myNumber);
    printf("Memory address %p\n", &myNumber);
    printf("Memory address using pointer %p\n", ptr);

    return 0;
}