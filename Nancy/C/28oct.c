/*
HW:
1. Take 10 integer inputs from user and store them in an array. Again ask user to give a number. Now, tell user whether that number is present in array or not.
2. Take 20 integer inputs from user and print the following:
number of positive numbers
number of negative numbers
number of odd numbers
number of even numbers
number of 0.
3. Take 10 integer inputs from user and store them in an array. Now, copy all the elements in another array but in reverse order.
4. Write a program to find the sum of all elements of an array.
5. Write a program to find the product of all elements of an array.
6. Make a Program to check whether the given array is a 'palindrome array' or not.
    * An array is a palindrome if you get the same array even after reversing it.
7. Write a C program that stores 10 user-given numbers in an array and then gives choice to the user to do one of the following actions:
    1. Print all prime numbers of the array
    2. Print sorted array in ascending order
    3. Print sorted array in decending order
    4. Print all the perfect numbers of the array
*/
// Sorting an array in ascending order:
#include<stdio.h>

int main()
{
    int a[8], i, temp, j;
    // Taking inputs & storing them into the array
    printf("Enter 5 integers:\n");  //6,5,3,1,8,7,2,4
    for(i=0; i<8; i++)
    {
        scanf("%d", &a[i]);
    }
    // sorting the array
    for(i=0; i<8; i++)
    {
        for(j=0; j<8-j; j++)
        {
            if(a[i] > a[i+1])
            {
                temp = a[i];
                a[i] = a[i+1];
                a[i+1] = temp;
            }
        }
    }
    // Printing the sorted array
    for(i=0; i<8; i++)
    {
        printf("%d\t", a[i]);
    }
    return 0;
}

// Next Lecture: How to create an array of user-defined size