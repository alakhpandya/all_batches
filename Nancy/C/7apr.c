#include<stdio.h>
float average(int n1, int n2)
{
    float ans;
    ans = (n1 + n2)/2.0;
    printf("The average of %d and %d = %0.3f", n1, n2, ans);
    return ans;
}
int main()
{
    int a, b, c, d;
    float ans;
    printf("Enter two integers:\n");
    scanf("%d%d", &a, &b);  //  a = 25, b = 35
    // average(5, 20);
    // average(a, b);
    printf("\nEnter two more integers:\n");
    scanf("%d%d", &c, &d); 
    // average(c, d);
    ans = average(a, b) + average(c, d);
    printf("Addition of averages = %.3f", ans);
    return 0;
}
/*
Classwork:
1. Write a C function that prints the factorial of a number given in its argument. Write a main program that takes 5 itegers from user and prints their factorials using that function.
*/