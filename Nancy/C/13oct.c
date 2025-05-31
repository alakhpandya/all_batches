/*
Make a C program that takes salaries of 5 employees from user then, ask user which employee's salary does she want to see and prints that employee's salary.
*/
#include<stdio.h>

int main()
{
    int a, b, c, d, e, choice;
    printf("Enter salaries of 5 employees:\n");
    scanf("%d %d %d %d %d", &a, &b, &c, &d, &e);
    printf("Which employee's salary do you want to see? Enter the serial no of employee: ");
    scanf("%d", &choice);
    switch(choice)
    {
        case 1:
            printf("Salary of employee 1 is: %d", a);
            break;
        case 2:
            printf("Salary of employee 2 is: %d", b);
            break;
        case 3:
            printf("Salary of employee 3 is: %d", c);
            break;
        case 4:
            printf("Salary of employee 4 is: %d", d);
            break;
        case 5:
            printf("Salary of employee 5 is: %d", e);
            break;
        default:
            printf("Employee with this serial number does not exist, please eneter a number from 1 to 5...");
    }
    return 0;
}
/*
Make a C program that takes marks of 10 students from user then, ask user which student's marks does she want to see and prints that student's marks.
*/