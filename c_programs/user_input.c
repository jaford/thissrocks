#include <stdio.h>

int main(){

    int myNum;
    printf("Enter a number: \n");

    // Similar to printf, scanf takes a user input!
    scanf("%d", &myNum);

    // To show this worked
    printf("Here is your number: %d", myNum);

    return 0;
}