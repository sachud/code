#include <stdio.h>

int main()
{
    int i = 8, j = 5;
    float x = 0.005, y = -0.01;
    char c = 'c', d = 'd';

    printf("a) %d\n", (3 * i - 2 * j) % (2 * d - c));
    printf("b) %d\n", 2 * ((i / 5) + (4 * (j - 3)) % (i + j - 2)));
    printf("c) %d\n", -(i + j));
    printf("d) %d\n", ++i);

    i = 8; j = 5; // reset values
    printf("e) %d\n", i++);

    i = 8; j = 5;
    printf("f) %d\n", --j);

    x = 0.005;
    printf("g) %.2f\n", ++x);

    y = -0.01;
    printf("h) %.2f\n", y--);

    i = 8; j = 5;
    printf("i) %d\n", i <= j);
    printf("j) %d\n", c > d);
    printf("k) %d\n", x >= 0);
    printf("l) %d\n", (i > 0) && (j < 5));
    printf("m) %d\n", (i > 0) || (j < 5));
    printf("n) %d\n", (x > y) && (i > 0) || (j < 5));
    printf("o) %d\n", (x > y) && (i > 0) && (j < 5));

    return 0;
}