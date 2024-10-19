/*
Write a C program that takes Names, height and marks in 3 subjects for 5 students and prints name, height & percentage of the tallest and the brightest student.
*/
#include<stdio.h>
#include<stdlib.h>

struct Student{
    char name[50];
    int height;
    float marks[3], percentage;
};

int main()
{
    struct Student s[5];
    int i, j, max_height, max_height_student;
    printf("Enter details of 5 students:\n");
    for ( i = 0; i < 5; i++)
    {
        printf("Student-%d:\n", i);
        printf("Name: ");
        fflush(stdin);
        gets(s[i].name);
        printf("Height: ");
        scanf("%d", &s[i].height);
        printf("Marks:\n");
        for ( j = 0; j < 3; j++)
        {
            printf("Subject %d: ", j);
            scanf("%f", &s[i].marks[j]);
        }
    }
    max_height = s[0].height;
    max_height_student = 0;
    for ( i = 1; i < 5; i++)
    {
        if (max_height < s[i].height)
        {
            max_height = s[i].height;
            max_height_student = i;
        }
    }
    printf("Details of the tallest student:\n");
    printf("Name: %s\n", s[max_height_student].name);
    printf("Height: %d\n", s[max_height_student].height);
    printf("Marks:\n");
    for ( i = 0; i < 3; i++)
    {
        printf("Subject %d: %0.2f\n", i, s[max_height_student].marks);
    }
    return 0;
}