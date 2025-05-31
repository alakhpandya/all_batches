// Operators in C
/*
1. Arithmetic Operators
    +
    -
    *
    /   11/4 => 2.75 or 2 (for integer division)
    %   Modulo => Returns remainder produced after integer division 11 % 4 => 3

2. Comparision / Relational / Conditional Operators: These operators will always return either True(1) or False(0)
    <       3 < 5 => True (1); 5 < 3 => False (0)
    >       a > b
    <=
    >=
    ==      a == 5 => is value in a 5? Yes (True/1) or No (False/0)
            a = 5 => Store 5 in a.
    !=      not equals to

*/
#include<stdio.h>
int main()
{
    /*
    int a = 11, b = 4;
    printf("%d/%d = %f\n", a, b, a/(float)b);     // typecasting
    printf("%d modulo %d = %d\n", a, b, a % b);     // typecasting
    return 0;
    */
   /*
   int total, years, r, months, days;
   printf("Enter number of days you want to convert in years/months/days: ");
   scanf("%d", &total);
   years = total/365;
   r = total % 365;
   months = r / 30;
   days = r % 30;
   printf("%d days = %d years, %d months and %d days", total, years, months, days);
   return 0;
   */
    int a, b;
    printf("Enter two integers: ");
    scanf("%d %d", &a, &b);
    printf("a > b is %d", a > b);
    return 0;
}

// convert 1010 days into years, months & days