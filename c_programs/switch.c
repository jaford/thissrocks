#include <stdio.h>

int main(){

    int day = 8;

    switch (day)
    {
    case 1:
        printf("Monday");
        // This breaks out of each code block if it is not or is executed.
        break;
    case 2:
        printf("Tuesday");
        break;
    case 3:
        printf("Wednesday");
        break;
    case 4:
        printf("Thursday");
        break;
    case 5:
        printf("Friday");
        break;
    case 6:
        printf("Saturdat");
        break;
    case 7:
        printf("Sunday");
        break;
    // No break needed for this due to this like a else in python.
    // This executes if no other conditions are met. 
    default:
        printf("There is no day in the number speficfied");
    }
    return 0;
}