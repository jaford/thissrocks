#include <stdio.h>

int main(){

    int i = 0; 

    // An exmple of a while loop to print out a number 
    // from 0 to 10!
    // As you see it indexs from 0 (or whatever you set it to) to the
    // The parameter you set it too! 
    while (i < 11) {
        printf("%d\n", i);
        // This the increase operator. 
        // If this not here the loop will go on and on! 
        i++;
    }
    return 0;
}