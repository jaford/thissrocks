#include <stdio.h>

int main(){

    int myNumber = 45;

    printf("Here is my number %d\n", myNumber);
    // Remeber that this outputs the address of memory for data.
    // This is read as hexadecimal

    // A pointer is a variable that stores the memory 
    // address of another variable as its value.
    printf("Memory address %p\n", &myNumber);

    return 0;

}
