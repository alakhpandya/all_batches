/*
HW: Write a C program to take names of 5 students in an array and print the name of the student given by user (Use two dimensional array)
*/
#include<stdio.h>

int main()
{
    char name[5][50];
    int i, stu;
    printf("Enter names of 5 students:\n");
    for(i=0; i<5; i++)
    {
        gets(name[i]);
    }
    printf("Which student's name do you want to print? Enter sr. no: ");
    scanf("%d", &stu);
    printf("Name of student-%d: %s", stu, name[stu]);
    return 0;
}
/*
Write a C code that takes names, marks & height of 5 students and prints all the data of the student given by user.
*/