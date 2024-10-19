// Recursive Functions: A function that calls itself is called recursive functions
/*
factorial function:
5! = 5 x 4!
4! = 4 x 3!
3! = 3 x 2!
2! = 2 x 1!
1! = 1 x 0!
0! = 1

Two steps
    Step 1: 
        Basis Step:
        0! = 1
    
    Step 2:
        Inductive Step (Recursive Step):
        if not 0:
        n! = n*(n-1)!

#include<stdio.h>
int recursiveFactorial(int n)
{
    if (n == 0)
    {
        return 1;
    }
    else
    {
        return n*recursiveFactorial(n-1);
    }
}

int main()
{
    int number, fact;
    printf("Enter any number:");
    scanf("%d", &number);
    fact = recursiveFactorial(number);
    printf("%d! = %d", number, fact);
    return 0;
}
*/
