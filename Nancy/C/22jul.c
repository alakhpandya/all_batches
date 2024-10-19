/*
Datatypes in C (Premitive/Basic)
Datatype                    Size in Bytes   Format Specifier
int                         2 or 4          %d, %i
long int                    4               %ld, %li
long long int               8               %lld, %lli

float                       4               %f
double                      8               %lf
long double              10, 12 or 16       %Lf

char                        1               %c

*/
#include<stdio.h>
int main()
{
    int a;
    long int b;
    long long int c;
    float d;
    double e;
    long double f;
    char g;
    printf("Enter 3 integers and 3 float numbers and 1 character: ");
    scanf("%d %ld %lld %f %lf %Lf %c", &a, &b, &c, &d, &e, &f, &g);
    printf("size of int = %d\n", sizeof(a));
    printf("size of long int = %d\n", sizeof(b));
    printf("size of long long int = %d\n", sizeof(c));
    printf("size of float = %d\n", sizeof(d));
    printf("size of double = %d\n", sizeof(e));
    printf("size of long double = %d\n", sizeof(f));
    printf("size of char = %d\n", sizeof(g));
    return 0;
}