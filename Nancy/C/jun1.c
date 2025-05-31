#include<stdio.h>

int main()
{
    int a = 7, *ptr_a;
    float b, *pb;
    ptr_a = &a;
    pb = &b;
    printf("a = %d\n", a);
    // printf("Address of a = %d\n", &a);
    // printf("Address of a = %x\n", &a);
    printf("Address of a = %p\n", &a);
    printf("ptr_a = %p\n", ptr_a);
    printf("Address of b = %p\n", &b);
    printf("pb = %p\n", pb);

    printf("Enter b: ");
    scanf("%f", pb);
    printf("b = %f\n", b);
    printf("b = %f\n", *pb);
    return 0;
}