#include<stdio.h>
/*
int main()
{
    int a, b, sum;
    int *pa, *pb, *psum;
    pa = &a;
    pb = &b;
    psum = &sum;            // psum = 5Bc23
    printf("Enter two integers:\n");
    scanf("%d%d", pa, pb);  //  5, 10
    // sum = a + b;
    *psum = *pa + *pb;       // psum = 15
    printf("%d + %d = %d", *pa, *pb, *psum);
    return 0;
}
*/
// Pointer Arithmetic
/*
int main()
{
    char a, *pa;
    int b, *pb;
    float c, *pc;
    double d, *pd;
    long double e, *pe;

    pa = &a;
    pb = &b;
    pc = &c;
    pd = &d;
    pe = &e;

    printf("Address of e = %p\n", pe);
    // pb++;
    pe = pe + 1;
    printf("Incremented address of e = %p\n", pe);
    return 0;
}
*/
// call by reference
void sum(int *pa, int *pb, int *ans)
// int sum(int *pa, int *pb)
{
    // int c;
    // c = *pa + *pb;
    // return c;
    *ans = *pa + *pb;
}

int main()
{
    int p, q, s;
    printf("Enter two integers:\n");
    scanf("%d%d", &p, &q);
    sum(&p, &q, &s);
    printf("%d + %d = %d", p, q, s);
    return 0;
}
/*
Write a C program that takes two integers and store their average in a variable. Print it. Use call by reference.
*/