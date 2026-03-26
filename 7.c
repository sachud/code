#include <stdio.h>
int main() {
    int num;

    printf("Enter a number: ");
    scanf("%d", &num);

    if (num % 5 == 0)
        printf("The number is a multiple of 5\n");
    else
        printf("The number is not a multiple of 5\n");
 
    if (num % 7 == 0 && num % 11 != 0)
        printf("The number is divisible by 7 but not by 11\n");
    else
        printf("The number does not satisfy the condition (divisible by 7 but not by 11)\n");

    return 0;
}