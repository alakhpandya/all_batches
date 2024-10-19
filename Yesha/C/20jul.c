#include<stdio.h>
int main()
{
    int a, b, c, d, e, f;
    printf("Enter 6 numbers: ");
    scanf("%d %d %d %d %d %d", &a, &b, &c, &d, &e, &f);
    /*
    if (a > b)
    {
        printf("a > b\n");
    }
    if (c > d)
    {
        printf("c > d\n");
    }
    if (e > f)
    {
        printf("e > f\n");
    }
    */
    if (a > b)
    {
        printf("a > b\n");
    }
    else if (c > d)
    {
        printf("c > d\n");
    }
    else if (e > f)
    {
        printf("e > f\n");
    }
    else
    {
        printf("Thanks!");
    }
 
    return 0;
}
/*
Class work:
1. Take 3 integers from the user & print the greatest out of them on the screen.

Home Work:
1. A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
    Ask user for quantity
    Suppose, each unit costs 100.
    Judge and print total cost for user.

2. A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
Ask user for their salary and year of service and print the net bonus amount.

3. A school has following rules for grading system:
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A
Ask user to enter marks and print the corresponding grade.

4. Write a C program to print absolute vlaue of a number entered by user. E.g.-
        INPUT:  13        OUTPUT: 13
        INPUT: -12        OUTPUT: 12

5. A student will not be allowed to sit in exam if his/her attendence is less than 75%.
    Take following input from user
        Number of classes held
        Number of classes attended.
    And print
        percentage of class attended
        Whether the student is allowed to sit in exam or not.

*/