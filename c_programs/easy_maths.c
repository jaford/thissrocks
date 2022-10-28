#include <stdio.h>

int main(){

    int x = 5;
    int y = 5;
    int sum = x + y;
    int sub = x - y;
    int multi = x * y;


    printf("%d\n", sum);
    printf("%d\n", sub);
    printf("%d\n", multi);

    // You can also string one line of variables to call that as well
    // Also learned that you can not declare a variable that has already been used!
    int num1 = 5, num2 = 10, num3 = 20;
    printf("%d\n", num1 + num2 + num3);
    return 0;

}