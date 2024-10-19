/*
HW:
1. Write a C program that takes Marks, Height and Fees of 5 students from user and then print the Marks, Height and Fees of the student with least marks, the tallest student and the student paying highest fees.

2. Write a C program to store names of 5 students and print them all.
*/
// How to take string input in C:
#include<stdio.h>
#include<stdlib.h>
/*
int main()
{
    // Yesha
    char name[50];
    int x = 5;
    // x = 13;
    // x = 29;
    int x[3];

    printf("x = %d\n", x);
    printf("Now enter your name: ");
    scanf(" %c", &name);
    printf("Your name is: %c", name);
    return 0;
}
*/
/*
int main()
{
    char name[50];
    int i, len;
    printf("How long is your name? ");
    scanf("%d", &len);      // 5
    printf("Enter your name: ");
    fflush(stdin);
    for ( i = 0; i < len; i++)
    {
        scanf("%c", &name[i]);
    }
    printf("Your name is: ");
    for ( i = 0; i < len; i++)
    {
        printf("%c", name[i]);
    }
    printf("\nThanks for using our program!");
    return 0;
}
*/
/*
int main()
{
    char name[50];
    printf("Enter your name: ");
    scanf("%s", name);
    printf("Your name is: %s", name);
    return 0;
}
*/
/*
int main()
{
    char name[50];
    printf("Enter your name: ");
    gets(name);
    printf("Your name is: %s", name);
    return 0;
}
*/
// Write a C program to store names of 3 students and print them all.
int main()
{
    char name[3][50];
    int i;
    for(i=0; i<3; i++)
    {
        printf("Enter name of student-%d: ", i);
        gets(name[i]);
    }
    for(i=0; i<3; i++)
    {
        printf("Name of student-%d: %s\n", i, name[i]);
    }
    return 0;
}