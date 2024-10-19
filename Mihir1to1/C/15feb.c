/*
User defined array
*/

#include<stdio.h>
int main(int argc, char const *argv[])
{
    int size, i, salary[100], choice;
    //taking size
    while (1)
    {
        printf("Please enter size: ");
        scanf("%d", &size);
        if (size > 100)
        {
            printf("\nSorry! Maximum allowed size is 100! Try again...\n");
        }
        else
        {
            break;
        }
    }
    //taking input in the array
    for ( i = 0; i < size; i++)
    {
        printf("Salary %d: ", i);
        scanf("%d", &salary[i]);
    }
    //taking choice input
    while (1)
    {
        printf("Please enter the employee number whose salary you want to see: ");
        scanf("%d", &choice);
        if (choice >= size)
        {
            printf("\nSorry! choice can not greater than size! Try again...\n");
        }
        else
        {
            break;
        }
    }
    //printing output
    printf("The salary of employee %d is: %d", choice, salary[choice]);
    return 0;
}
/*
Make a C program that takes marks of 5 students (stu0, stu1, stu2, stu3, stu4) for 
their 4 subjects (sub0, sub1, sub2, sub3) and prints the marks of the chosen 
subject of chosen student.
*/