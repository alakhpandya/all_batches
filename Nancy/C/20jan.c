/*
Write a program that takes marks, height and fees of 5 students and then ask user what does she want to do:
to print the details of the student with highest marks or
to print the details of the tallest student or
to print the details of the student paying highest fees.
Print the output accordingly.
*/
#include<stdio.h>
int main()
{
    int s[5][3], i, j, max, h_marks;
    for(i=0; i<5; i++)
    {
        printf("Enter the marks, height and fees of student-%d\n", i);
        // scanf("%d %d %d", &s[i][0], &s[i][1], &s[i][2]);
        for(j=0; j<3; j++)
        {
            scanf("%d", &s[i][j]);
        }
    }
    
    /*
    for(i=0; i<5; i++)
    {
        printf("Marks, Height and Fees of student-%d\n", i);
        for(j=0; j<3; j++)
        {
            printf("%d\n", s[i][j]);
        }
    }
    */

    max = s[0][0];  // assigning first student's marks to max
    h_marks = 0;
    for(i=1; i<5; i++)
    {
        if (s[i][0] > max)
        {
            max = s[i][0];
            h_marks = i;
        }
    }
    printf("Details of the student with highest marks:\n");
    printf("student-%d:\n",h_marks);
    printf("Marks: %d\n", s[h_marks][0]);
    printf("Height: %d\n", s[h_marks][1]);
    printf("Fees: %d\n", s[h_marks][2]);
    return 0;
}