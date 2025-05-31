#include<stdio.h>

int fact(int n){
    int f = 1, i;
    for(i = 1; i <= n; i++){
        f = f * i;
    }
    // printf("\n%d! = %d", n, f);
    return f;
}
int main()
{
    int arr[5], i, sum = 0;
    printf("Enter 5 integers:\n");
    for ( i = 0; i < 5; i++)
    {
        scanf("%d", &arr[i]);
    }

    for ( i = 0; i < 5; i++)
    {
        // fact(arr[i]);
        sum = sum + fact(arr[i]);
    }
    printf("sum of factorials = %d", sum);
    return 0;
}


// Class work:
/*
1. Write a function that returns the absolute sum of two integers given in its argument. Write a main program that asks 4 integers from user. Use the function and print absolute sum of first & second number as well as 3rd & 4th number. Absolute sum of two integers is making both of them positive and then adding them.
eg, 
absolute sum of 5 & -3 = 5 + 3 = 8
absolute sum of -5 & -3 = 5 + 3 = 8
absolute sum of -5 & 3 = 5 + 3 = 8
absolute sum of 5 & 3 = 5 + 3 = 8

2. Write a function that returns the absolute sum of two integers given in its argument. In the main program, you will be given an array of 10 transactions (credit/debit) of a bank customer. Credits are marked as positive integers while debits are marked as negatives. Use your function and print the total amount transacted by the customer. Only print the total transacted amount.
eg,
[20, -10, 30, -50, 15, 25, -20, 8, -2, 10]
output:
total amount transacted = 190
*/