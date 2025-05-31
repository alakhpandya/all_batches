/*
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
    printf("Enter 3 integers, 3 floating point numbers and 1 character: ");
    scanf("%d %ld %lld %f %lf %Lf %c", &a, &b, &c, &d, &e, &f, &g);
    printf("\nint : %d, \t\t\tsize : %d", a, sizeof(a));
    printf("\nlong int : %ld, \t\t\tsize : %d", b, sizeof(b));
    printf("\nlong long int : %lld, \t\t\tsize : %d", c, sizeof(c));
    printf("\nfloat : %f, \t\t\tsize : %d", d, sizeof(d));
    printf("\ndouble : %lf, \t\t\tsize : %d", e, sizeof(e));
    printf("\nlong double : %Lf, \t\t\tsize : %d", f, sizeof(f));
    printf("\nchar : %c, \t\t\tsize : %d", g, sizeof(g));
    return 0;
}
*/

// Operators in C
/*
1. Arithmetic Operators:
    +   a + b => adds a & b
    -   a - b => subtract b from a
    *   a * b => multiplies a with b
    /   a / b => divides a by b;         11 / 4 = 2
    %   a % b => returns remainder produced by dividing a by b;  11 % 4 => 3

2. Comparision Operators/Relational Operators: They will always return either True(1) or False(0)
    <   3 < 5 => True; 5 < 3 => False   
    >
    <=
    >=
    ==  a == 5 => will return true if a is equal to 5. we check for equality.
        a = 5  => will set value 5 into variable a (Assignment)
    !=  a != 7 => will return True if a is not equal to 7.

3. Assignment Operators:
    =
        a = 5
         <--
        5 + 3 = b       WRONG
             <--
        
        b = 5 + 3       RIGHT
         <--
*/
#include<stdio.h>
int main()
{
    int a = 3, b = 5;
    // printf("%d\n", a < b);
    // printf("%d\n", b < a);
    printf("%d\n", a == 5);
    return 0;
}