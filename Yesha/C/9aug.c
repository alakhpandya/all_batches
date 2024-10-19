// while loop
/*
#include<stdio.h>

int main()
{
    int i;
    i = 1;
    while (i <= 10)
    {
        printf("Yesha is a good girl.\n");
        i++;
    }

    for(i = 1; i <= 10; i++)
    {
        printf("Yesha is a good girl.\n");
    }

    return 0;
}
*/
/*
1. Make a C program that takes a number from user and prints multiplicative table of that number till the number specified by user.
2. Modify the above program to produce output for the range given by user.
3. Make a C program that counts and prints the number of digits in the number given by user.
number  digits
37234     5
                    Counter
37234/10 => 3723        1
3723/10 => 372          2
372/10 => 37            3
37/10 => 3              4
3/10 => 0.3 = 0         5
*/
#include<stdio.h>
int main()
{
    int i, number, counter=0;
    printf("Enter any integer: ");
    scanf("%d", &number);
    // for(i = number; i > 0 ; i = i/10)
    while (number > 0)
    {
        number = number/10;
        counter++;
    }
    printf("number of digits = %d", counter);
    return 0;
}
/*
i   Condition True?     Execution
1       Y               1
2       Y               2
3       Y               3
4       Y               4
*/