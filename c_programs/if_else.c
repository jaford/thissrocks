#include <stdio.h>

int main(){
    if (60 > 30) {
        printf("60 is greater than 30!\n");
    }

    int x = 40;
    int y = 30;
    if (x > y) {
        printf("x is greater than y!\n");
    }

    int time = 20;
    if (time < 10) {
        printf("Good Day!\n");
    } else {
        printf("A okay day!\n");
    }

    int time_2 = 22;
    if (time_2 < 10) {
    printf("Good morning.\n");
    } else if (time_2 < 20) {
    printf("Good day.\n");
    } else {
    printf("Good evening.\n");
    }
    return 0;
}