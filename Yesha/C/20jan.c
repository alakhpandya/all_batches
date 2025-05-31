/*
Write a C program that takes Marks, Height and Fees of 5 students from user and then print the Marks, Height and Fees of the student with highest marks.
*/
#include<stdio.h>
int main()
{
    int report_card[5][3], i, j, max;
    for(i=0; i<5; i++){
        printf("Enter the marks, height & fees of student-%d:\n", i);
        for(j=0; j<3; j++)
        {
            scanf("%d", &report_card[i][j]);
        }
    }
    max = report_card[0][0];
    student = 0;
    for(i=1; i<5; i++)
    {
        if (report_card[i][0] > max)
        {
            max = report_card[i][0];
            student = i;
        }
    }
    printf("Details of student with Top Marks: \n");
    printf("Marks: %d", report_card[student][0]);
    printf("Height: %d", report_card[student][1]);
    printf("Fees: %d", report_card[student][2]);
    return 0;
}