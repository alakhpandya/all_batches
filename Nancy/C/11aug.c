// Loops in C:
/*
We use loops when we want to execute an instruction or set of instructions multiple times. 
And, we put only those instructions inside the loop which we want to execute multiple times.

Types of Loops:
1. Entry control loops: for loop & while loop
2. Exit control loops: do while loop
*/
#include<stdio.h>

int main()
{
    int i;
    for (i = 1; i <= 10; i++)
    {
        printf("Nency is a good girl.\n");
    }
    return 0;
}
/*
i   i <= 5     Execution   
1   T           1           
2   T           2
3   T           3
4   T           4
5   T           5
6   F           X
i=0; i<10; i++     =>  11
i = -10; i<=-1; i++  =>  16
i=1; i<=20; i=i+2   =>  10
i=1; i<=1000000000; i=i*10  =>  2
i=2; i<1100; i=i*2  =>  10 
*/