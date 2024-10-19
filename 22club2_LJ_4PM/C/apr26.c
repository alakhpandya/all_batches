#include<stdio.h>
/*
int main()
{
    int a = 20, *pa;
    char b, *pb;
    float c;
    float *pc = &c;
    pa = &a;
    pb = &b;
    // scanf("%d", &a);
    printf("a = %d\n", a);
    printf("Address of a (in decimal) = %d\n", &a);
    printf("Address of a (in hex) = %x\n", &a);
    printf("Address of a (as an address) = %p\n", &a);
    printf("Address of a (through pa): %p\n", pa);
    pa++;
    printf("Incremented pa: %p\n", pa);
    printf("pb : %p\n", pb);
    pb++;
    printf("Incremented pb : %p\n", pb);

    return 0;
}


            Turbo   VS
short int   2       2
int         2       4
long int    4       4

1. Write a code to store an integer & a float. Print their addresses using pointers.
2. 

*/

/*
int main()
{
    int a = 10;
    int *pa = &a;
    printf("a = %d\n", a);
    printf("Address of a: %p\n", pa);
    printf("value of a using pointer: %d\n", *pa);
    // * = reference operator
    // & = address operator
    return 0;
}
*/

// write a program to add two integers using their pointers
int main()
{
    int a, b, sum;
    int *pa = &a, *pb = &b, *psum = &sum;
    printf("Enter two integers:\n");
    scanf("%d%d", pa, pb);
    *psum = *pa + *pb;
    printf("sum = %d", *psum);
    return 0;
}