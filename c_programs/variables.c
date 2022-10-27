// Rule of thumb for variables
// type variableName = value;
#include <stdio.h>


int main(){
    // Declare the variable
    int my_number = 10;
    float my_float = 5.52;
    char my_char ='H';

    // Format Specifiers
    // for int you must use a specifier to print out the variable value
    // The two for a int are %i or %d
    // use %c for char and %f for float
    printf("%f\n", my_float);
    printf("%d\n", my_number);
    printf("%c\n", my_char);
    return 0;
}

