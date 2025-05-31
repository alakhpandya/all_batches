/*
1. Check whether a number given by user is prime or not.
*/
#include<stdio.h>

int main()
{
    int n, i, prime=1;
    // printf("n = %d\n", n);
    printf("Enter any number: ");
    scanf("%d", &n);
    for (i = 2; i < n ; i++)
    {
        if (n % i == 0)
        {
            printf("%d is not a prime number because it is divisible by %d", n, i);
            prime = 0;
            break;
        }
    }
    if (prime == 1)
    {
        printf("%d is a Prime number.", n);
    }
    return 0;
}
/*
HW:
1. Write a C program to read the age of a candidate and determine whether it is eligible for casting his/her own vote.

2. Write a C program to accept a coordinate point in a XY coordinate system and determine in which quadrant the coordinate point lies.
    eg if x = 7 & y = 9 the person is in 1st quadrant
    if x = -7 & y = 9 the person is in 2nd quadrant
    if x = 7 & y = -9 the person is in 3rd quadrant
    if x = -7 & y = -9 the person is in 4th quadrant

3. Write a C program to calculate the root of a Quadratic Equation.
    Additional Info:    
        if a = 0; roots don't exist
        if b^2 - 4*a*c < 0, roots are imaginary
        otherwise, roots of a quadratic equation are: 
        [-b + sqrt(b^2 - 4*a*c)]/(2*a) and [-b - sqrt(b^2 - 4*a*c)]/(2*a)

4. Write a C program to read temperature in centigrade and display a suitable message according to temperature state below :
    Temp < 0 then Freezing weather
    Temp 0-10 then Very Cold weather
    Temp 10-20 then Cold weather
    Temp 20-30 then Normal in Temp
    Temp 30-40 then Its Hot
    Temp >=40 then Its Very Hot
        Test Data :
        42
        Expected Output :
        Its very hot.
*/