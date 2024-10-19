/*
Write a C program that takes Marks, Height and Fees of 5 students from user and then print the Marks, Height and Fees of the given student.
*/
#include<stdio.h>
int main()
{
    int report_card[5][3], i, j;
    for(i=0; i<5; i++){
        printf("Enter the marks, height & fees of student-%d:\n", i);
        // scanf("%d %d %d", &report_card[i][0], &report_card[i][1], &report_card[i][2]);
        for(j=0; j<3; j++)
        {
            scanf("%d", &report_card[i][j]);
        }
    }
    for ( i = 0; i < 5; i++){
        printf("Marks, height and fees of student-%d are:\n", i);
        // printf("%d\n", report_card[i][0]); 
        // printf("%d\n", report_card[i][1]); 
        // printf("%d\n", report_card[i][2]); 
        for(j=0; j<3; j++){
            printf("%d\n", report_card[i][j]); 
        }
    }
    return 0;
}