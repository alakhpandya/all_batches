/*
1. Make a C program find & print all the factors of a given positive integer.
2. Make a C program that asks two numbers from user and prints all the prime numbers between those two numbers.

Create the following programs using while loop:

3. A number is called perfect number if all of its factors (except itself) sums up to that number. for example, 6 is a perfect number. Because factors of 6 are: 1, 2, 3, 6
Except 6, if we add other factors: 1 + 2 + 3 = 6.
Make a C program that asks two numbers from user & prints all the perfect numbers between those two numbers.

4. A 3-digit number is called armstrong number if cubes of all of its digits sums up to that number. eg, 153 is an armstrong number as, 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
Make a C program that asks two numbers from user & prints all the armstrong numbers between those two numbers.

*/
#include<stdio.h>

int main()
{
    int x, p, prime=1;
    printf("Enter any number: ");
    scanf("%d", &x);    // x= 17
    for(p = 2; p < x; p++)
    {
        if (x % p == 0) // 15 % 2 == 0?
        {
            printf("not prime.\n");
            prime = 0;
            break;
        }
    }
    if (prime == 1)
    {
        printf("It's Prime.\n");
    }
    return 0;
}