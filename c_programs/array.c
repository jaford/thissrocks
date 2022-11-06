#include <stdio.h>

int main(){

    int array[] = {10, 20, 30, 40};

    // You can access the array by using the variable you assigned it. 
    // You have to indacate a index of said array to display the amount.
    printf("%d\n", array[0]);

    // You can also change a value in the array by calling the variable...
    // Then you indacate the index then set it to a new value.
    array[0] = 99;
    printf("%d\n", array[0]);

    int i;
    
    printf("Here is my array\n");
    for (i = 0; i < 4; i++) {
        printf("%d\n", array[i]);
    }

    return 0;
}