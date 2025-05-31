/*
We use loops when we want to execute similar instruction(s) multiple
times.

1. Entry Control Loops:
    for loop
    while loop
2. Exit control loops:
    do-while loop

Elements of any loop:
1) Iterator initialization
2) Termination condition
3) Changing the value of iterator inside the loop.

You can do all the tasks even using only one of these loop as well.
Choice of for loop/while loop are given for convinience.

#include<stdio.h>
int main()
{
    int number, i;
    printf("Please enter any number: ");
    scanf("%d", &number);
    // for(i=1; i<=10; i++), for(i=11; i<20; i++), for(i=10; i>0; i--)
    // for(i=2; i<=20; i=i+2), for(i=1; i<=1000000000 ;i=i*10)
    for(i=0; i<10; i++)
    {
        printf("%d x %d = %d", number, i-10, number*(i-10));
    }
    return 0;
}
Make a C program that takes an integer from the user and prints the
sum of all integers from 0 to that number on the scree.
Sample input:
7
Expected output:
1 + 2 + 3 + 4 + 5 + 6 + 7 = 28
*/
//Nesting of blocks::
/* Make a C program to print triangle of * of height given
by user.
Sample input: 5
Expected output:
    *
   * *
  * * *
 * * * *
* * * * *

*/